#!/usr/bin/swift

import Foundation

func initialInput() -> [Int] {
    let text = try! String(contentsOfFile: "day2.txt")
    let arrText = text.components(separatedBy: ",").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredArrText = arrText.filter{ $0 != "" }
    return filteredArrText.map {return Int($0) ?? 0}
}

func runProgram(_ input: [Int]) -> [Int] {
    var arrInt = input
    for i in stride(from: 0, to: arrInt.count, by: 4) {
        let opCode = arrInt[i]
        // print("opCode: \(opCode)")

        switch opCode {
        case 1:
            let indexForFirstInput = arrInt[i + 1]
            let indexForSecondInput = arrInt[i + 2]
            let indexForStorage = arrInt[i + 3]
            arrInt[indexForStorage] = arrInt[indexForFirstInput] + arrInt[indexForSecondInput]
            // print("add")
        case 2:
            let indexForFirstInput = arrInt[i + 1]
            let indexForSecondInput = arrInt[i + 2]
            let indexForStorage = arrInt[i + 3]
            arrInt[indexForStorage] = arrInt[indexForFirstInput] * arrInt[indexForSecondInput]
            // print("mult")
        case 99:
            // print("HALT")
            return arrInt
        default:
            print("ERROR—————————ERROR—————————ERROR—————————ERROR")
        }
    }
    return arrInt
}

func day2_pt1() -> [Int] {
    var arrInt = initialInput()
    arrInt[1] = 12
    arrInt[2] = 2

    return runProgram(arrInt)
}

func day2_pt2() -> Int {
    let desiredValue = 19690720

    for i in 0...99 {
        for j in 0...99 {
            var arrInt = initialInput()
            arrInt[1] = i
            arrInt[2] = j

            if runProgram(arrInt)[0] == desiredValue {
                print("i: \(i), j: \(j), answer: \(100 * i + j)")
                return 100 * i + j
            }
        }
    }
    return 0
}

print("Part 1: \(day2_pt1())")
print("Part 2: \(day2_pt2())")
