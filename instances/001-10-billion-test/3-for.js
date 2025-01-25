var numbers = []
start_time = performance.now()
for( i=0;i<10**9;i++){
  numbers.push(i)
  if(numbers.length == (10**8)+1){
    numbers = []
  }
}
console.log(numbers.length)
end_time = performance.now()
console.log("the script took:",(end_time-start_time)/1000,"seconds")
console.log(numbers[numbers.length-1])
