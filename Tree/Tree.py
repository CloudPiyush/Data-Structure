class TreeNode:

    def __init__(self,Data) -> None:
        self.Data = Data
        self.Children = []
        self.Parent = None

    def Get_Length(self):
        Level = 0
        P = self.Parent
        while P:
            Level += 1
            P = P.Parent
        return Level
    
    def Get_Skills(self,skill):
        skill.Parent = self
        self.Children.append(skill)

    def Show_Skills(self):
        Space = ' ' * self.Get_Length() *3
        Prefix = Space + '|__' if self.Parent else ''
        print(Prefix + self.Data)
        if self.Children:
            for skill in self.Children:
                skill.Show_Skills()

def Get_Details():
    root = TreeNode('Shivram Patil')

    Ajit_Patil = TreeNode('Ajit Patil')
    Ajit_Patil.Get_Skills(TreeNode('Piyush Patil'))
    Ajit_Patil.Get_Skills(TreeNode('Ranjeet Patil'))

    Ranjeet_Patil = TreeNode('Ranjeet Patil')
    Ranjeet_Patil.Get_Skills(TreeNode('Siddhi'))
    Ranjeet_Patil.Get_Skills(TreeNode('Riddhi'))

    Dada = TreeNode('Baburao Dada')
    Dada.Get_Skills(Ajit_Patil)
    Dada.Get_Skills(Ranjeet_Patil)

    Shrikant_Patil = TreeNode('Shrikant Patil')
    Shrikant_Patil.Get_Skills(TreeNode('His Daughter.'))

    Anil_Patil = TreeNode('Anil Patil')
    Anil_Patil.Get_Skills((Shrikant_Patil))

    Gibhu = TreeNode('Ganpat Gibhu')
    Gibhu.Get_Skills(Anil_Patil)


    Vilas_Patil = TreeNode('Vilas Patil')
    Vilas_Patil.Get_Skills(TreeNode('Sai Patil'))

    Appa = TreeNode('Raghunath Appa')
    Appa.Get_Skills(Vilas_Patil)

    Ravindra_Patil = TreeNode('Ravindra Patil')
    Ravindra_Patil.Get_Skills(TreeNode('Sahili Patil'))
    Ravindra_Patil.Get_Skills(TreeNode('Neha Patil'))
    Ravindra_Patil.Get_Skills(TreeNode('Sonu Patil'))

    Swapnil_Patil = TreeNode('Swapnil Patil')
    Swapnil_Patil.Get_Skills(TreeNode('Ananya Patil'))

    Kishor_Patil = TreeNode('Kishor Patil')
    Kishor_Patil.Get_Skills((Swapnil_Patil))
    Kishor_Patil.Get_Skills(TreeNode('Bhaiya'))

    Anna = TreeNode('Baburao Dada')
    Anna.Get_Skills(Ravindra_Patil)
    Anna.Get_Skills(Kishor_Patil)

    root.Get_Skills(Dada)
    root.Get_Skills(Gibhu)
    root.Get_Skills(Appa)
    root.Get_Skills(Anna)
    root.Show_Skills()

if __name__ == "__main__":
    Get_Details()