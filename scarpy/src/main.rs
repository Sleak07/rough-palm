// file opener for image files

use std::path::Path;
use anyhow::Result;
use image::io::Reader;

fn get_image_dimensions(file_path: &str) -> Result<(u32, u32)> {
    let path = Path::new(file_path);
    let reader = Reader::open(path)?;
    let dimensions = reader.into_dimensions()?;
    Ok(dimensions)
}    
fn main (){
    match get_image_dimensions("data/sample.jpg") {
        Ok((width, height)) => println!("dimensions: {} x {}", width, height),
        Err(e) => println!("error: {}", e),
    }
    
}
