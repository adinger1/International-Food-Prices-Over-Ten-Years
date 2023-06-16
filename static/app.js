
function updateBoxplot(country){
  traceNum = 0
  url = "http://127.0.0.1:5000/api/v1.0/domestic_change/" + country + "/boxplot"
  d3.json(url).then(function(data){

    let yAxisLabels = []
    let traces = []
    for(i = 0; i < data.length; i++){
      let row = data[i]
      yAxisLabels.push(row[1])

      let trace1 = {
      x: [row[2],row[3],row[4]],
      type: 'box',
      name: row[1]
      };

      traces.push(trace1)
      traceNum++
    }

    console.log(yAxisLabels)

    var layout = {
      title: 'Commodity Price Ranges for ' + country,
      xaxis:{
        title: 'Price ($)'
      },
      yaxis:{
        tickangle:-45
      }
    }

    Plotly.newPlot('box', traces, layout); 
  })      
}


function updateLinegraphs(country){
  url = "http://127.0.0.1:5000/api/v1.0/domestic_change/" + country + "/lineplot"
  d3.json(url).then(function(data){
    //data = all countries + commodities
    let x_times = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
    let y_traces = []
    
    url2 = "http://127.0.0.1:5000/api/v1.0/domestic_commodities/" + country
    d3.json(url2).then(function(data2){
      //data2 = commodities for each country

      for(i = 0; i < data2.length; i++){
        let commodity = data2[i][0]
        let y_values = []
        //Iterate through all 
        for(j=0; j< data.length; j++){
          if(data[j][2] == commodity){
            console.log(data[j][2])
            y_values.push(data[j][3])
          }
        }

        let trace = {
          x:x_times,
          y:y_values,
          type: 'scatter',
          name: commodity
        }

        y_traces.push(trace)
      }

      var layout = {
        title: 'Commodities for ' + country + ' Over 10 Years',
        xaxis:{
          title: 'Time (Years)'
        },
        yaxis:{
          title: "Cost ($)"
        }
      };
      Plotly.newPlot('linechart',y_traces,layout)
    })
    
  })
}

function commodityLinegraph(){
  url = "http://127.0.0.1:5000/api/v1.0/int_commodity_list"
  d3.json(url).then(function(commodities){
    let x_times = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
    let y_traces = []
    
    url2 = "http://127.0.0.1:5000/api/v1.0/int_commodity_data"
    d3.json(url2).then(function(commodity_data){
      
      for(i = 0; i < commodities.length; i++){
        let commodity = commodities[i][0]

        //Not all commodities have data for 2020 so we will extract the x_values from the returned data
        let y_values = []
        //Iterate through all 
        for(j=0; j< commodity_data.length; j++){
          if(commodity_data[j][0] == commodity){
            y_values.push(commodity_data[j][2])
          }
        }

        let trace = {
          x:x_times,
          y:y_values,
          type: 'scatter',
          name: commodity
        }

        y_traces.push(trace)
      }

      var layout = {
        title: 'International Commodity Prices',
        xaxis:{
          title: 'Time (Years)'
        },
        yaxis:{
          title: "International Cost ($)"
        }
      };
      Plotly.newPlot('line2',y_traces,layout)
    })
    
  })
}

function updateBar(){
  url1 = "http://127.0.0.1:5000/api/v1.0/bar_2010"
  url2 = "http://127.0.0.1:5000/api/v1.0/bar_2020"
  let x_countries = []
  let y1 = []
  let y2 = []

  d3.json(url1).then(function(data){
    for(i = 0; i < data.length; i++){
      x_countries.push(data[i][1])
      y1.push(data[i][3])
    }
  })

  d3.json(url2).then(function(data){
    for(i = 0; i < data.length; i++){
      y2.push(data[i][3])
    }

    let trace1 = {
      x: x_countries,
      y:y1,
      type:'bar',
      name: 'Prices in 2010'
    }
  
    let trace2 = {
      x: x_countries,
      y:y2,
      type:'bar',
      name:'Prices in 2020'
    }
  
    var traces = [trace1,trace2]
    let layout = {
      title: "Wheat Price Differences from 2010 to 2020",
      barmode: 'group',
      xaxis: {
        type: 'category',
        title: 'Country'
      },
      yaxis:{
        title: "Domestic Cost ($)"
      }
    }
  
    Plotly.newPlot('groupbar',traces,layout)
  })

  console.log(x_countries)
  console.log(y1)
  console.log(y2)
  
}


function optionChanged(country){
  url = "http://127.0.0.1:5000/api/v1.0/domestic_change/" + country + "/boxplot"
  d3.json(url).then(function(data){
    updateBoxplot(country)
    updateLinegraphs(country)
  });
}

function init() {
  //Creating dropdown menu
  let dropdownMenu1 = d3.select("#selDataset1");

  let url1 = "http://127.0.0.1:5000/api/v1.0/box_country_list"
  d3.json(url1).then(function(data){
    for(i = 0; i < data.length; i++){
      dropdownMenu1.append("option").attr("value", data[i][0]).text(data[i][0]);
    }
    
    optionChanged(data[0][0]);
  });

  updateBar()
  commodityLinegraph()
}   
    

init();