function loadmusic(url, tid){
	var tjid = '#'+tid;
	$.ajax({type:'GET',
        url: url, // the pyramid server
        data: '',
        contentType: 'application/json; charset=utf-8',
        success: function(data){

        	var myPlaylist = [
        	                  {
        	                      mp3:'/static/music/'+data["musicfile"],
        	                	  //mp3: "https://raw.githubusercontent.com/kaiwang0112006/music/master/private/alliask_adele.mp3",
        	                      title:data["musicname"],
        	                      cover:'/static/images/music/jing.jpg'
        	                  }
        	              ];

            $(tjid).ttwMusicPlayer(myPlaylist, {
                autoPlay:false, 
                description:"music",
                jPlayer:{
                	swfPath:'../swf/jquery_jplayer' //You need to override the default swf path any time the directory structure changes
                }
            });
        }	
	});
}