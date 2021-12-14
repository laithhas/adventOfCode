#!/usr/bin/swift

import Foundation

func day1_pt1() -> Int {
    let text = try! String(contentsOfFile: "day1.txt")
    let arrText = text.components(separatedBy: "\n").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredArrText = arrText.filter{ $0 != "" }
    let arrInt = filteredArrText.map {return Int($0) ?? 0}
    let setInts = Set( arrInt.map { $0} )
    for i in arrInt {
        if setInts.contains(2020 - i) {
            return (2020 - i) * i
        }
    }
    return 0
}

func day1_pt2() -> Int {
    let text = try! String(contentsOfFile: "day1.txt")
    let arrText = text.components(separatedBy: "\n").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredArrText = arrText.filter{ $0 != "" }
    let arrInt = filteredArrText.map {return Int($0) ?? 0}
    let setInts = Set( arrInt.map { $0} )
    for i in arrInt {
        for j in arrInt {
            if setInts.contains(2020 - i - j) {
                return (2020 - i - j) * i * j
            }
        }
    }
    return 0
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
