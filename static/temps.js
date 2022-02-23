async function getTemps() {
    const response = await fetch('/boiler/monitor');
    const temps = await response.body;
    return temps; 
    
  }