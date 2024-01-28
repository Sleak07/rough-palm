// file opener for image files
use image ::GenericImageView;

fn main(){
    let img = image::open("galaxy.png").unwrap();

    println!("dimensions {:?}", img.dimensions());
}
