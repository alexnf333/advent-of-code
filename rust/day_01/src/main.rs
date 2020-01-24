use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};
use std::time::Instant;
#[macro_use(c)]
extern crate cute;

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

// calculate total fuel and return processing time
fn calculate_fuel() -> f64 {
    let mut fuel_for_spacecraft = 0;
    let mut fuel_for_all_fuel = 0;
    let now = Instant::now();

    let spacecraft = lines_from_file("data.txt");
    for module in spacecraft {
        let module = module.parse::<i32>().unwrap();
        let module_fuel = ((module / 3) as i32) - 2;
        fuel_for_spacecraft = fuel_for_spacecraft + module_fuel;
        let mut fuel_for_fuel = module_fuel;
        loop {
            fuel_for_fuel = ((fuel_for_fuel / 3) as i32) - 2;
            if fuel_for_fuel <= 0 {
                break;
            }
            fuel_for_all_fuel = fuel_for_all_fuel + fuel_for_fuel;
        }
    }

    let new_now = Instant::now();
    let elapsed_time = new_now.duration_since(now).as_micros() as f64;
    println!("fuel for spacecraft: {}", fuel_for_spacecraft);
    println!("fuel for fuel: {}", fuel_for_all_fuel);
    println!("total fuel: {}", fuel_for_spacecraft + fuel_for_all_fuel);
    println!("elapsed time: {}", elapsed_time);
    elapsed_time
}

// calculate average proccesing time for the indicated number of tests
fn main() {
    const NUMBER_OF_TESTS: u8 = 100;
    let tests_array = c![calculate_fuel(), for _x in 0..NUMBER_OF_TESTS];
    let sum: f64 = tests_array.iter().sum();
    println!("average time: {} microseconds", sum / NUMBER_OF_TESTS as f64);
}
