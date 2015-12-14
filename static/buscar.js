angular.module('myApp').controller('buscar', ['$scope','$http','$location',function ($scope,$http,$location) {
    var ctrl = this;
    $scope.Videos = [];
    var videos = [];

    ctrl.init = function(){
        $.ajax({
            
		
			url: '/FindVideosChannelGet',
			type: 'GET',
			success: function(response){
                $scope.Videos=jQuery.parseJSON(response);
                console.log($scope.Videos);
                for(var j=0;j<$scope.Videos.length;j++){
                    $("#TableS").find('tbody')
                        .append($('<tr>')
                            .append($('<td>')
                                .append($scope.Videos[j].title)
                                
                            )
                            .append($('<td>')
                                
                                .append($scope.Videos[j].description)
                                
                            )
                        );
                            
                }
                
			},
			error: function(error){
				console.log(error);
			}
    });
    }
    ctrl.init();
    $scope.buscar= function(){
        var videoname = $('#txtname').val();
         $.ajax({
			url: '/FindVideosChannel',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
                $scope.Videos=jQuery.parseJSON(response);
                console.log($scope.Videos);
                $("#TableS").find("tr:gt(0)").remove();
                for(var j=0;j<$scope.Videos.length;j++){
                    $("#TableS").find('tbody')
                        .append($('<tr>')
                            .append($('<td>')
                                .append($scope.Videos[j].title)
                                
                            )
                            .append($('<td>')
                                
                                .append($scope.Videos[j].description)
                                
                            )
                        );
                            
                }
                
			},
			error: function(error){
				console.log(error);
			}
    });                                     
    };
}]);