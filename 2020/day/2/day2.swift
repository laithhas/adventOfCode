#!/usr/bin/swift

import Foundation

func day1_pt1() -> [String] {
    let text = try! String(contentsOfFile: "day2.txt")
    let arrText = text.components(separatedBy: "\n").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredArrText = arrText.filter{ $0 != "" }
    return filteredArrText
}

func day1_pt2() -> Int {
    return 0
}

print(day1_pt1())
print(day1_pt2())
