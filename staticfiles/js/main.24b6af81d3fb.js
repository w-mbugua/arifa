$(document).ready(function(){

    $('.replybtn').click(function(e){
      e.preventDefault();
      console.log('aye')
      $('.reply-box').toggle()
    })
    console.log('ready!')
    $('a.followbutton').click(function(event){
      event.preventDefault()
      console.log('whoooosh')
     
      $.post("/profile/follow/",{
        id: $(this).data('id'),
        action: $(this).data('action')

      },
      function(data){
        console.log(data)
        if(data['status'] == 'ok'){
          var prev_action = $('a.followbutton').data('action');

          $('a.followbutton').data('action', prev_action == 'follow' ? 'unfollow' : 'follow');

          $('a.followbutton').text(prev_action == 'follow' ? 'Unfollow' : 'Follow');

          var prev_followers = parseInt($('span.total').text());
          console.log("followers",prev_followers)

          $('span.total').text(prev_action == 'follow' ? prev_followers + 1 : prev_followers - 1);
        }
      }
      )
    })

    $('a.likebutton').click(function(e){
      e.preventDefault();
      console.log('we likey!')
      $.post('/posts/like/',{
        id: $(this).data('id'),
        action: $(this).data('action')
      },
      function(data){
        console.log(data)
        if(data['status'] == 'ok'){
          var previous_action = $('a.likebutton').data('action');

          $('a.likebutton').data('action', previous_action == 'like' ? 'unlike' : 'like');

          $('a.likebutton').text(previous_action == 'like' ? 'Unlike' : 'Like');

          var prev_likes = parseInt($('span.count').text());
          console.log("LIKES",prev_likes)
          $('span.count').text(previous_action == 'like' ? prev_likes + 1 : prev_likes - 1);

        }
      }
      )
    })
    
})