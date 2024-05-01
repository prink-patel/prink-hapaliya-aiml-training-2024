start_detection();
const socket =io.connect('http://127.0.0.1:5001');
async function start_detection(){
    // Access the webcam and send frames to the backend
    camera_stream = await navigator.mediaDevices.getUserMedia({ video: true })

    const video = document.createElement('webcamFeed');
    video.srcObject = camera_stream;

    const track = camera_stream.getTracks()[0];
    const imageCapture = new ImageCapture(track);

    frames_interval = setInterval(() => {
        imageCapture.grabFrame()
        .then(imageBitmap => {
        const canvas = document.createElement('canvas');
        canvas.width = imageBitmap.width;
        canvas.height = imageBitmap.height;
        const context = canvas.getContext('2d');
        context.drawImage(imageBitmap, 0, 0);
        const frameData = canvas.toDataURL('image/jpeg');
        socket.emit('send_frame', { "frame": frameData });
        })
        .catch(error => console.error(error));
    },100)

    socket.on('send_frame_js', data => {
        const processedFrame = document.getElementById('preview');
        const base64String = data["frame"];
        processedFrame.src = 'data:image/jpeg;base64,' + base64String;
    });
}



