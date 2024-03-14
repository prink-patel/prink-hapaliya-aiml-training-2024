import cv2
import numpy as np


def dic(lines_list):
    groups={}
    for i in lines_list:
        x1,y1 = i[0]
        x2,y2 = i[1]
        if x2-x1 == 0:
            slope = 0
        else:
            slope = round((y2-y1)/(x2-x1),1)

        if slope in groups:
            groups[slope].append(tuple((i[0],i[1])))
        else:
            groups[slope] = [tuple((i[0],i[1]))]
    return groups


def find_slop(lines_list):
    x1,y1 = lines_list[0]
    x2,y2 = lines_list[1]
    if x2-x1 == 0:
        slope = 0
    else:
        slope = round((y2-y1)/(x2-x1),1)
    return slope


# Read image
image = cv2.imread('hex1.png')

height = image.shape[0]
width = image.shape[1]
# Convert image to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(gray,50,150,apertureSize=3)

# Apply HoughLinesP method to 
# to directly obtain line end points
lines_list =[]
lines = cv2.HoughLinesP(
			edges, # Input edge image
			1, # Distance resolution in pixels
			np.pi/180, # Angle resolution in radians
			threshold=100, # Min number of votes for valid line
			minLineLength=5, # Min allowed length of line
			maxLineGap=10 # Max allowed gap between line for joining them
			)

for points in lines:
	x1,y1,x2,y2=points[0]
	cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
	lines_list.append([(x1,y1),(x2,y2)])



list_hex=np.array([(58, 0),(0, 106),(58, 208),(181, 208),(240, 106),(181, 0)])

mask = np.zeros(image.shape, dtype=np.uint8)

channel_count = image.shape[2]

ignore_mask_color = (255,) * channel_count

cv2.fillPoly(mask, [list_hex], ignore_mask_color)
# apply the mask

marked_image = cv2.bitwise_and(image, image, mask=mask[:, :, 0])


a,b=lines_list[4][0][0],lines_list[4][1][1]
dic_slop=dic(lines_list)

slop=find_slop(lines_list[4])

gray = cv2.cvtColor(marked_image,cv2.COLOR_BGR2GRAY)
output = np.zeros((height*3,width*3,image.shape[2]),np.uint8)
output[:marked_image.shape[0],:marked_image.shape[1],:]+=marked_image
    
min=9999
print(lines_list)
max_height=0
for i in lines_list:
    if max_height<i[0][1]:
        max_height=i[0][1]
    elif max_height<i[1][1]:
        max_height=i[1][1]
    
    
for i in lines_list:
    slop=find_slop(i)
    res = tuple(map(lambda i, j: abs(i - j), dic_slop[slop][1][0], dic_slop[slop][0][0]))
    # print(res,res1)
    final=res
    if min >res[1] and slop>0 and (res[1]-max_height)>0:
        min=res[1]
        output[final[1]-max_height:final[1]-max_height+marked_image.shape[0],final[0]:final[0]+marked_image.shape[1],:]+=marked_image  
        # output[200-final[1]:200-final[1]+marked_image.shape[0],final[0]+200:200+final[0]+marked_image.shape[1],:]+=marked_image  
    elif slop<0:
        print(res)
        output[final[1]:final[1]+marked_image.shape[0],final[0]:final[0]+marked_image.shape[1],:]+=marked_image
    elif slop==0:
        print(res,"1")
        output[final[1]:final[1]+marked_image.shape[0],final[0]:final[0]+marked_image.shape[1],:]+=marked_image

# cv2.imwrite("output.png",output)



cv2.imshow("gfsfdg",output)
cv2.waitKey(0)
cv2.destroyAllWindows()