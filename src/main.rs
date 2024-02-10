use image::GenericImageView;

fn main() {
    // opening the image
    let img = image::open("galaxy.png").unwrap();

    // checking the dimensions
    println!("dimensions {:?}", img.dimensions());

    // color type of image
    println!("{:?}", img.color());
}
