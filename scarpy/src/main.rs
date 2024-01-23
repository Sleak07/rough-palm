fn main (){

    let response = reqwest :: blocking:: get("https://demo.opencart.com");// getting 

    let data = response.unwrap().text().unwrap();


    println!("{data}")
    

    // using structs to store data

        struct DemoProduct {
        image: Option<String>,
        url: Option<String>,
        title: Option<String>,
        description: Option<String>,
        new: Option<String>,
        tax: Option<String>,
    }
    let mut demo_products: Vec<DemoProduct> = Vec::new();
    
    
}
