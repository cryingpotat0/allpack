from interface import Language, Runner
from modal import Image


class RustRunner(Runner):
    def get_lang(self) -> Language:
        return Language.RUST

    def get_image(self) -> Image:
        return Image.from_registry(
                "rust:1.73.0-buster",
                add_python="3.11",
            )

    def get_default_files(self) -> dict[str, str]:
        return {
        "Cargo.toml": """
[package]
name = "hello-world"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
hashbrown = "0.14"
""",
        "src/main.rs": """
fn main() {
    println!("Hello, world!");
    println!("Hello, world2 !");
    let mut map = hashbrown::HashMap::new();
    map.insert(1, 2);
    println!("Hello, world3 !");
    println!("Hello, world4 {:?}!", map);
}
""",
        }

    def get_default_command(self) -> str:
        return "cargo run"

