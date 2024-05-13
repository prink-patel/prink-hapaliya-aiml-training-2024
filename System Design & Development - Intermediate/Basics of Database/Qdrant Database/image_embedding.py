from urllib.request import urlopen
from PIL import Image
import timm


class ImageEmbedding:
    def __init__(self):
        pass
    def run(self, img):
        """using haggingface model to get image vectors 

        Args:
            img : PIL image object used to read image

        Returns:
            output (list): vectors values 
        """
        img = Image.open(urlopen(
            'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
        ))
        model = timm.create_model(
            'convnextv2_base.fcmae',
            pretrained=True,
            num_classes=0,
        )
        model = model.eval()
        data_config = timm.data.resolve_model_data_config(model)
        transforms = timm.data.create_transform(**data_config, is_training=False)
        output = model(transforms(img).unsqueeze(0))
        output = model.forward_features(transforms(img).unsqueeze(0))
        output = model.forward_head(output, pre_logits=True)
        
        return output[0].tolist()