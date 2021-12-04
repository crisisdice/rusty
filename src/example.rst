fn main() {
    struct Test {
        a: u64,
        b: u64
    }
    
    const FACTOR: Test = { Test {
        a: 12,
        b: 13
       }
    };
    
    let x = FACTOR.a + FACTOR.b;
    println!("{}", x);
}
