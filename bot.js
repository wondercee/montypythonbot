setInterval(function() {
  try {
    run();
  }
  catch (e) {
    console.log(e);
  }
}, 60000* 60);
