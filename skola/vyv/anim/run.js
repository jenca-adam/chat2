$('body').append($('<button>SPUSTI ANIMACIU</button>'))
$('button').click(function(){
var theme = new Audio('music/theme.wav');
theme.volume=0.3;
theme.play();
$('body').append($('<img src="assets/forest.png" id="poz" style="min-width:100%;bottom:0px;position:fixed;">'))
$('body').append($('<img src="assets/knight.gif" id="knight" style="bottom:100px;left:0px;transform:scale(0.6);position:absolute;">'))
$('body').append($('<img src="assets/datel.ico" id="datel-im" style="top:0px;left:0px;position:absolute;">'))

$('button').hide(0);
start();
})


