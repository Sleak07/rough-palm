// file opener for image files
use image ::GenericImageView;

fn main(){
    // opening the image file
    let img = image::open("galaxy.png").unwrap();

    // getting the image file dimensions
    println!("dimensions {:?}", img.dimensions());

    // getting the image color
    println!("{:?}",img.color());

    
}
