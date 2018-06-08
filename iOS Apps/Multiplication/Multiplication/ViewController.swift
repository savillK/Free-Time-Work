//
//  ViewController.swift
//  Multiplication
//
//  Created by Savill Khemraj on 2018-06-07.
//  Copyright © 2018 Savill Khemraj. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var firstInt = 0
    var secondInt = 0
    var product = 0
    
    
    @IBOutlet weak var numberOne: UILabel!
    
    
    @IBOutlet weak var numberTwo: UILabel!
    
    
    @IBOutlet weak var result: UILabel!
    
    
    @IBAction func showAnswer(_ sender: Any) {
        product = firstInt * secondInt
        result.text = String(product)
    }
    
    @IBAction func next(_ sender: Any) {
        nextIntegers()
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        nextIntegers()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    //Generate random numbers and set appropriate labels
    func nextIntegers() {
        firstInt = Int(arc4random_uniform(UInt32(21)))
        secondInt = Int(arc4random_uniform(UInt32(21)))
        
        numberOne.text = String(firstInt)
        numberTwo.text = String(secondInt)
        
        result.text = "Result"
    }


}

