#!/usr/bin/swift

import Foundation

/**
TO-DOs:
    - Fix assumption that everything is in the positive quadrant
    - Fix board sizing algorithim to include negatives
    - Figure out what to do with central port
*/

func parsedInitialInput() -> [[String]] {
    let text = try! String(contentsOfFile: "day3.txt")
    let textArrays = text.components(separatedBy: "\n").map { $0.trimmingCharacters(in: .whitespaces)}
    let filteredTextArrays = textArrays.filter{ $0 != "" }
    let groupedArrays = filteredTextArrays.map { return [$0] }
    return groupedArrays.map {
        return $0[0].components(separatedBy: ",").map { $0.trimmingCharacters(in: .whitespaces)}
    }
}

// ——— struct ———

struct ElectricPanel {

  enum Unit: String {
    case empty = "."
    case vertical = "|"
    case horizontal = "-"
    case centralPort = "o"
    case corner = "+"
    case intersection = "X"
  }

  var board : [[Unit]]

  mutating func setUnit(x: Int, y: Int, newValue: Unit) {
    let oldValue = board[y][x]
    switch oldValue {
    case .empty:
        board[y][x] = newValue
    case .vertical:
        board[y][x] = .intersection
    case .horizontal:
        board[y][x] = .intersection
    case .centralPort:
        board[y][x] = newValue
    case .corner:
        board[y][x] = .intersection
    case .intersection:
        board[y][x] = newValue
    }
  }

  init(input: [[String]]) {
    let firstWire = input[0]
    let secondWire = input[1]

    // First wire
    var horizontalSize1 = 1
    var verticalSize1 = 1
    for direction in firstWire {
        let dir = direction[0]
        let index = direction.index(direction.endIndex, offsetBy: -1 * (direction.count - 1))
        let mySubstring = direction[index...]
        let count = Int(mySubstring)!
        // let count = Int(String(direction[1]))!
        switch dir {
        case "R":
            horizontalSize1 += count
        case "D":
            break
        case "L":
            break
        case "U":
            verticalSize1 += count
        default:
            print("dang")
        }
    }

    // Second wire
    var horizontalSize2 = 1
    var verticalSize2 = 1
    for direction in secondWire {
        let dir = direction[0]
        let index = direction.index(direction.endIndex, offsetBy: -1 * (direction.count - 1))
        let mySubstring = direction[index...]
        let count = Int(mySubstring)!
        switch dir {
        case "R":
            horizontalSize2 += count
        case "D":
            break
        case "L":
            break
        case "U":
            verticalSize2 += count
        default:
            print("dang")
        }
    }

    // Board size
    let boardHorizontalSize = max(horizontalSize1, horizontalSize2)
    let boardVerticalSize = max(verticalSize1, verticalSize2)

    board = Array(repeating: Array(repeating: .empty, count: boardHorizontalSize), count: boardVerticalSize)
    board[0][0] = .centralPort
    // var cursor = (0, 0)
    // for direction in firstWire {
    //     let dir = direction[0]
    //     let count = Int(String(direction[1]))!
    //     switch dir {
    //     case "R":
    //         for _ in 1...count - 1 {
    //             cursor.1 += 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .horizontal)
    //         }
    //         cursor.1 += 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     case "D":
    //         for _ in 1...count - 1 {
    //             cursor.0 -= 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .vertical)
    //         }
    //         cursor.0 -= 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     case "L":
    //         for _ in 1...count - 1 {
    //             cursor.1 -= 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .horizontal)
    //         }
    //         cursor.1 -= 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     case "U":
    //         for _ in 1...count - 1 {
    //             cursor.0 += 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .vertical)
    //         }
    //         cursor.0 += 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     default:
    //         print("dang")
    //     }
    // }

    // cursor = (0, 0)
    // for direction in secondWire {
    //     let dir = direction[0]
    //     let count = Int(String(direction[1]))!
    //     switch dir {
    //     case "R":
    //         for _ in 1...count - 1 {
    //             cursor.1 += 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .horizontal)
    //         }
    //         cursor.1 += 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     case "D":
    //         for _ in 1...count - 1 {
    //             cursor.0 -= 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .vertical)
    //         }
    //         cursor.0 -= 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     case "L":
    //         for _ in 1...count - 1 {
    //             cursor.1 -= 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .horizontal)
    //         }
    //         cursor.1 -= 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     case "U":
    //         for _ in 1...count - 1 {
    //             cursor.0 += 1
    //             setUnit(x: cursor.1, y: cursor.0, newValue: .vertical)
    //         }
    //         cursor.0 += 1
    //         setUnit(x: cursor.1, y: cursor.0, newValue: .corner)
    //     default:
    //         print("dang")
    //     }
    // }
  }
}

extension ElectricPanel: CustomStringConvertible {

  var description: String {
    return board.map { row in row.map { $0.rawValue }.joined(separator: " ") }
        .joined(separator: "\n") + "\n"
  }
}

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}

// ——— struct ———

func day3_pt1() -> [Int] {
    return [0]
}

func day3_pt2() -> Int {
    return 0
}

print(parsedInitialInput())
print(ElectricPanel(input: parsedInitialInput()))
// print("Part 1: \(day3_pt1())")
// print("Part 2: \(day3_pt2())")
