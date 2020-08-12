window.onload = function() {
localConnection = new RTCPeerConnection()
  console.log('ss')
  var width = 320;    // We will scale the photo width to this
  var height = 0;     // This will be computed based on the input stream

  var streaming = false;

  var video = null; 


  video = document.getElementById('video') 

  navigator.mediaDevices.getUserMedia({video:true, audio:false})
  .then(function(stream) {
  		video.srcObject = stream
  		console.log(stream) 
  		// console.log(stream.getVideoTracks()) 
  		// console.log(stream.addTrack()) 
  		// console.log(stream.getTracks()[0]) 
  		console.log(stream.addTrack(stream.getTracks()[0])) 
  		console.log(stream) 
  		
  		video.play() 
  })
  .catch(function(err) {
        console.log("An error occurred: " + err);
    })
}