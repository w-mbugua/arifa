$(document).ready(function(){
    console.log('ready!')
    $(".upload-btn").click(function(){
        $("#div_id_image").toggle()
    })

    $(".post-btn").click(function(event){
        event.preventDefault();

        var serializedData = $(".post-form").serialize()
        console.log(serializedData)

        $.ajax({
            url: $(".post-form").attr("action"),
            data: serializedData,
            type: $(".post-form").attr("method"),
            success: function(response){
                console.log(response.data[0])
                console.log(response.data[0].author)
                console.log(response.data[0].body)
                $("#posts-box").prepend(
                    `<div class="card">
                    <div class="card-header">
                      ${response.data[0].author}
                    </div>
                    <div class="card-body">
                      <blockquote class="blockquote mb-0">
                        <p>${response.data[0].body}</p>
                        <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
                      </blockquote>
                    </div>
                  </div>`
                )
            }
        })
        $(".post-form")[0].reset()
    })
})