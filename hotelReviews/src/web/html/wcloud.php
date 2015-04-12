<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
    <script type="text/javascript" src="js/d3.layout.cloud.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  </head>
  <body>
<script>
function getURLParameter(name) {
      return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
}

function drawwc(){
    
var fill = d3.scale.category20();
  d3.layout.cloud().size([2000, 2000])
      .words(items)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
      .start();

  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", 2000)
        .attr("height", 2000)
      .append("g")
        .attr("transform", "translate(150,150)")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }

}
var url = "";
if(getURLParameter('flag')=="p"){
   url = "http://localhost:5000/hotelpc/"+getURLParameter('val');
}
else{

   url = "http://localhost:5000/hotelnc/"+getURLParameter('val');
}


var items =[];
    $.getJSON( url, function( data ) {
        $.each( data, function( key, val ) {
            $.each(val,function(data1){  items.push(val[data1]); });
            
            
        });
        drawwc();
    });


</script>
  </body>
</html>
