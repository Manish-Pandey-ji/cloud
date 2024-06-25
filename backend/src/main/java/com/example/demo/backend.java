//package com.example.demo;

//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.RestController;

//@RestController
//public class HelloController {

  //  @GetMapping("/hello")
    //public String hello() {
     //   return "Hello from the backend!";
//    }
//}

package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class backend{
	@GetMapping("/hello")
	public String hello(){
		return "Hello from the backend which is created by Manish Pandey";
	}
}

