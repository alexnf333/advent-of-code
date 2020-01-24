use std::fs;
use std::time::Instant;
#[macro_use(c)]
extern crate cute;
extern crate regex;

// calculate number of possible passwords and return processing time
fn possible_passwords() -> f64 {
    let mut given_range = [0, 0];
    let mut given_range_index = 0;
    let mut meet = 0;
    let mut doubles = false;
    let mut ascending_sequence = true;
    let mut larger_group = -1;
    let now = Instant::now();

    let passwords_range = fs::read_to_string("data.txt")
        .expect("Something went wrong reading the file");

    let passwords_range = &passwords_range[..passwords_range.len()-1];

    let re = regex::Regex::new(r"-").unwrap();
    for part in re.split(&passwords_range) {
        let range_limit = part.parse::<i32>().unwrap();
        given_range[given_range_index] = range_limit;
        given_range_index = given_range_index + 1;
    }

    for password in given_range[0]..given_range[1]+1 {
        let password_string: String = password.to_string();
        if password_string.len() != 6 {
            continue;
        }
        let char_vec:Vec<char> = password_string.chars().collect();
        for digit in 0..password_string.len()-1 {
            if char_vec[digit] == char_vec[digit+1] {
                if doubles == false {
                    if larger_group != 0 {
                        doubles = true;
                        larger_group = 0;
                    }
                } else {
                    larger_group = 1
                }
            } else {
                doubles = false;
                if char_vec[digit] > char_vec[digit+1] {
                    ascending_sequence = false;
                    continue;
                }
            }
        }
        if larger_group == 0 && ascending_sequence {
            meet = meet + 1;
        }
        doubles = false;
        ascending_sequence = true;
        larger_group = 1;
    }

    let new_now = Instant::now();
    let elapsed_time = new_now.duration_since(now).as_millis() as f64;
    println!("met-criteria passwords: {:?}", meet);
    println!("elpased time: {} milliseconds", elapsed_time);
    elapsed_time
}

// calculate average proccesing time for the indicated number of tests
fn main() {
    const NUMBER_OF_TESTS: u8 = 100;
    let tests_array = c![possible_passwords(), for _x in 0..NUMBER_OF_TESTS];
    let sum: f64 = tests_array.iter().sum();
    println!("average time: {} milliseconds", sum / NUMBER_OF_TESTS as f64);
}
