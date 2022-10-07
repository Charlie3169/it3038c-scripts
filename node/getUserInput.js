process.stdout.write("Hello. What is your name? ")

process.stdin.on('data', (data) => {
  console.log("Hello " + data.toString())
  process.exit()
});

process.on('exit', () => {
  console.log('Thanks for the info!')
});