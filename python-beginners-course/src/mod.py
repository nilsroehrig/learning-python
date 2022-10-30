import mod1
import data1
import data2 as nn
from mod1 import myName

mod1.welcome(data1.myName["first"], data1.myName["last"])
mod1.welcome(nn.myName["first"], nn.myName["last"])
mod1.welcome(myName["first"], myName["last"])
print(mod1.adder(2, 3))
