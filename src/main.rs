use image::{imageops, GenericImageView};

fn main() {
    // opening the image
    let img = image::open("galaxy.png").unwrap();

    // checking the dimensions
    println!("dimensions {:?}", img.dimensions());

    // color type of image
    println!("{:?}", img.color());

    // imageops in the image

    let bright_image = imageops::brighten(&img, 70);
    bright_image.save("brightened_galaxy.png").unwrap();
    println!("image saved successfuly");

    // flipping the image
    let flip = imageops :: flip_horizontal(&img);
    flip.save("flipped.png") .unwrap();
    println!("flipped successful");

    




}