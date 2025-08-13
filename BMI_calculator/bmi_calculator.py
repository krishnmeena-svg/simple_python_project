#Project: BMI Calculator
#Author: Krishn Meena
#Description: This program calculates the Body Mass Index (BMI) of a person using their weight and height and categorizes it based on WHO standards.

class BMICalculator:
    def __init__(self,name:str,weight:float, height:float):
        self.name=name
        self.weight=weight
        self.height=height
    
        
    def bmi_calculation(self):
      
    #Calculates the Body Mass Index (BMI) and returns the result.

    #Returns:
        #dict: If weight and height are valid, returns a dictionary with name, BMI value, and weight category.
        #str: If weight or height is invalid, returns an error message.
    
        if self.weight<=0 or self.height<=0:
            return "error-weight and height must be positive" 
            
        # category check
        bmi=self.weight/(self.height*self.height) #this calculate BMI
        bmi=round(bmi,2)
        
        if bmi<18.5:
            return {"name":self.name, "Body mass index":bmi,"Category":"Underweight"} 
            
        elif 18.5 <= bmi <= 24.9:
            return {"name":self.name, "Body mass index":bmi,"Category":"Normal"}
            
        elif 25 <= bmi <= 29.9:
            return {"name":self.name, "Body mass index":bmi,"Category":"Overweight"}
            
        else: 
            return {"name":self.name, "Body mass index":bmi,"Category":"Obese"}
            
person1=BMICalculator("krishn", 550,1.85)   
result=person1.bmi_calculation()

if isinstance(result,dict): 
    for key, value in result.items(): 
     print(f"{key}:{value}")
else: print(result)