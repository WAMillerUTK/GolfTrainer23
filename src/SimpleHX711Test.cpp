// MIT License
//
// Copyright (c) 2021 Daniel Robertson
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include "../include/common.h"

int main(int argc, char** argv) {

    using namespace std;
    using namespace HX711;

    const char* const err = "Usage: [DATA PIN] [CLOCK PIN] [REFERENCE UNIT] [OFFSET]";
    
    if(argc != 1) {
        cerr << err << endl;
        return EXIT_FAILURE;
    }

    const int dataPin = 2; //stoi(argv[1]);
    const int clockPin = 3; // stoi(argv[2]);
    const int refUnit = -337; // stoi(argv[3]);
    const int offset = 0; // stoi(argv[4]);

    SimpleHX711 hx(2, 3, refUnit, offset);
    // SimpleHX711 hx3(dataPin, clockPin, refUnit, offset);
    // SimpleHX711 hx4(dataPin, clockPin, refUnit, offset);

    ofstream ofile;
    ofile.open("tmp1.csv");

    if (ofile.fail()) return EXIT_FAILURE;

    for(int i = 0; i < 1000; ++i) {

        const Mass m = hx.weight(3);
	m.getValue();
	ofile << m.toString(Mass::Unit::LB) << endl;
        
        cout    << "\x1B[2J\x1B[H"
                << "\t" << m.getValue() << '\n'
   //             << "\t" << m1.toString(Mass::Unit::UG) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::MG) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::KG) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::TON) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::IMP_TON) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::US_TON) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::ST) << '\n'
                << "\t" << m.toString(Mass::Unit::LB) << '\n'
   //             << "\t" << m1.toString(Mass::Unit::OZ) << '\n'
                << endl;

    }

    return EXIT_SUCCESS;

}
