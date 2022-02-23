const bg_success = "badge rounded-pill bg-success"
const bg_danger = "badge rounded-pill bg-danger"

function check_badges_status(status){
  const badges = document.querySelectorAll('#chart2 span')
  // console.log(status)
  
  for (var ele in badges){
    let cls = badges[ele].classList
    let text = badges[ele].innerHTML

    if (status[ele] == true){
      let txt = text.replace('OFF', 'ON')
      cls = bg_success
      badges[ele].classList = cls
      badges[ele].innerHTML = txt
    }
  }
  for (var ele in badges){
    let cls = badges[ele].classList
    let text = badges[ele].innerHTML

    if (status[ele] == false){
      let txt = text.replace('ON', 'OFF')
      cls = bg_danger
      badges[ele].classList = cls
      badges[ele].innerHTML = txt
    }
  }
}

function getTemps() {
  var data_string = document.getElementById('boiler_data').value
  data_string = data_string.replace(/'/g, '"');
  data_string = data_string.replaceAll('T', 't');
  data_string = data_string.replaceAll('F', 'f');

  var data = JSON.parse(data_string)
  console.log(data)
  var options1 = {
    chart: {
      type: 'line'
    },
    series: [{
      name: 'feeder',
      data: data.feeder
    },
    {
      name: 'boiler',
      data: data.boiler_temp
    },
    {
      name: "boiler's return",
      data: data.boiler_return
    },
    {
      name: 'cwu',
      data: data.cwu
    },
    {
      name: 'co',
      data: data.co
    },
    ],
    xaxis:{
      labels: {
        show: true,
        rotate: -65,
        rotateAlways: false,
        hideOverlappingLabels: true,
        showDuplicates: false,
        trim: false,
        minHeight: undefined,
        maxHeight: 120,
      }, 
      categories: data.dates
    }
  }
  check_badges_status(data.devices)
  var chart1 = new ApexCharts(document.querySelector("#chart1"), options1);  
  chart1.render();
}

getTemps();