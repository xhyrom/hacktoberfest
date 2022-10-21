use std::io;

fn main() {
    println!(r#"
Hello, World!

Let's try to find the date where you were born on.
If my guess is lower, type 'l'.
If my guess is higher, type 'h'.
If my guess is correct, type 'y'.

Let's go

    "#);
   let int = binary_search();
    println!("\n\nYou were born on {} of some month!", int);
}

fn binary_search() -> i32 {
    let (mut low, mut high) = (1,31);
    let mut day = (low+high)/2;
    let mut buf = String::new();

loop {
  println!("I guess: {day}\nHigher or Lower?");
  io::stdin().read_line(&mut buf).unwrap();
  if &buf[..] == "y\n" {
    return day;
  } else if &buf[..] == "l\n" {
    low = day;
  } else {
    high = day;
  }
  day = (low + high) / 2;
  buf.clear();
}
}