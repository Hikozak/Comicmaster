var DragAndDrop = (function(){
    var galleryUploader;
    
    function init(){
        console.log("drag-and-drop ready!");
        
        galleryUploader = new qq.FineUploader({
            element: document.getElementById("fine-uploader-gallery"),
            template: 'qq-template-gallery',
            request: {
                endpoint: '/server/uploads'
            },
            thumbnails: {
                placeholders: {
                    waitingPath: '/js/placeholders/waiting-generic.png',
                    notAvailablePath: '/js/placeholders/not_available-generic.png'
                }
            },
            validation: {
                allowedExtensions: ['jpeg', 'jpg', 'gif', 'png']
            },
            callbacks: {
                onComplete: function(id, name, responseJSON, maybeXhr) {console.log(responseJSON)}
            }
        });
    }
    
    
    var public_api = {
        init: init
    };
    
    return public_api;
})();