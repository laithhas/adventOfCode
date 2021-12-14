#!/usr/bin/swift

import Foundation

func day1_pt1() -> Int {
    let text = try! String(contentsOfFile: "day1.txt")
    let arrText = text.components(separatedBy: "\n").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredArrText = arrText.filter{ $0 != "" }
    let arrInt = filteredArrText.map {return Int($0) ?? 0}
    let fuelForEachShip = arrInt.map { fuelCalc($0) }
    return fuelForEachShip.reduce(0, +)
}

func day1_pt2() -> Int {
    let text = try! String(contentsOfFile: "day1.txt")
    let arrText = text.components(separatedBy: "\n").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredArrText = arrText.filter{ $0 != "" }
    let arrInt = filteredArrText.map {return Int($0) ?? 0}
    let fuelForEachShip = arrInt.map({
        (value: Int) -> Int in
        var fuel = fuelCalc (value)
        var totalFuel = 0
        while fuel >= 0 {
            totalFuel += fuel
            fuel = fuelCalc(fuel)
        }
        return totalFuel
    })


    return fuelForEachShip.reduce(0, +)
}

func fuelCalc(_ value: Int) -> Int {
    return value.quotientAndRemainder(dividingBy: 3).0 - 2
}

print(day1_pt1())
print(day1_pt2())

// ------------------------------------------------------

// #!/usr/bin/swift

// import Foundation

// func day1_pt1() -> Int {
//     return 0
// }

// func day1_pt2() -> Int {
//     return 0
// }

// print(day1_pt1())
// print(day1_pt2())
