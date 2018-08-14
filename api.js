
// 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      // 3. This function creates an <iframe> (and YouTube player)
      //    after the API code downloads.
      var player;
      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
          height: '390',//390
          width: '640',//640
          videoId: 'U0D3AOldjMU', // decides which video it plays
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
      }
// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
      player.setVolume(75);
      event.target.playVideo(); //makes video play when it loads
}

function setTitle(){
  var data = player.getVideoData();
  var videoTitle = data.title;
  document.getElementById("Title").innerHTML = videoTitle;
}

function play() {
  player.playVideo();
}
function pause() {
  player.pauseVideo();
}

function video1() {//change videoId
player.loadVideoById('U0D3AOldjMU'); //loads vid without playing
}
function video2() {//change videoId
player.loadVideoById('ue80QwXMRHg'); //loads vid and plays automatically
//player.cueVideoById(); this loads without playing
}
function video3() {//change videoId
player.loadVideoById('xjDjIWPwcPU'); //loads vid without playing
}

function onPlayerStateChange(){
  setTitle();
}
