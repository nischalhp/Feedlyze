
var sampleData = {
  "question":"ques2",
  "answers":[
    {
        "label" : "yes",
        "value" : "40"
    },
    {
        "label" : "no",
        "value" : "60"
    }
  ]
};


nv.addGraph(function() {

    var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
       .y(function(d) { return d.value })
        .showLabels(true);
  
      d3.selectAll(".chart svg")
          .datum(sampleData.answers)
        .transition().duration(1200)
         .call(chart);
 
   return chart;
 });
 
 nv.addGraph(function() {

  var chart = nv.models.pieChart()
       .x(function(d) { return d.label })
       .y(function(d) { return d.value })
       .showLabels(true)
       .labelThreshold(.05)
       .donut(true);
 
     d3.selectAll(".chart2 svg")
         .datum(sampleData.answers)
       .transition().duration(1200)
         .call(chart);
 
   return chart;
 });
 