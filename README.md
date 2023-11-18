# Mutation Testing Report for Polynomial Class
## Introduction
A sophisticated software testing method called "mutation testing" entails making small changes to a program's source code, or "mutants," and then observing whether the test suite recognizes (or eliminates) these modifications. The procedure aids in assessing how well the test suite finds errors. An overview of the mutation testing done on the Polynomial class is given in this report.
## List of Defined Mutation Operators
The methods by which the source code is changed to create mutants are known as mutation operators. For the Polynomial class, the following mutation operators were defined:
1. Arithmetic Operator Replacement: Changing arithmetic operators (e.g., + to -, * to /).
2. Logical Connector Replacement: Altering logical connectors in conditionals (e.g., and to or).
3. Relational Operator Replacement: Modifying relational operators (e.g., > to <, == to !=).
4. Constant Replacement: Adjusting constant values in expressions.
5. Statement Removal: Removing specific statements or expressions.
