class Investment:
    def __init__(self, monthlyInvestment = 0, yearlyInterestRate = 0, years = 0) -> None:
        self.monthlyInvestment = monthlyInvestment
        self.yearlyInterestRate = yearlyInterestRate
        self.years = years
    
    def calculateFutureValue(self):
        monthlyInterestRate = self.yearlyInterestRate / 12 /100
        months = self.years * 12

        futureValue = 0
        for i in range(months):
            futureValue += self.monthlyInvestment
            monthlyInterestAmount  = futureValue * monthlyInterestRate
            futureValue += monthlyInterestAmount 
        return futureValue