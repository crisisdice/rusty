fn main() {
    fizzbuzz(15);
}

fn fizzbuzz(n: i32) {
    let mut index = 1;

    loop {
        let mut statement = String::from("");

        if index % 3 == 0 {
            statement.push_str("Fizz");
        }

        if index % 5 == 0 {
            statement.push_str("Buzz");
        }

        println!("{}: {}", index, statement);

        if index == n {
            break;
        }

        index += 1;
    }
}
