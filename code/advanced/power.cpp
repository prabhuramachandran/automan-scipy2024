#include <iostream>
#include <fstream>
#include <string>
using namespace std; 

int main(int argc, char* argv[]) {

    string filename;
    filename = argv[1];
    cout << "Start..." << endl;
    cout << filename << endl;

    std::ifstream myfile; myfile.open(filename);
    string outdir; myfile >> outdir; 
    float power; myfile >> power; 
    myfile.close();

    cout << outdir << " " << power << endl;
    cout << "End!" << endl;
    return 0;
}