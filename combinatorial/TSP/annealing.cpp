#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

float calculate_deltaE(vector<vector<float>>& matriz, int16_t* seq1, int16_t* seq2, int num_elements) {
    float deltaE = 0;
    for (int i = 0; i < num_elements - 1; i++) {
        int16_t element1A = seq1[i], element1B = seq1[i + 1];
        int16_t element2A = seq2[i], element2B = seq2[i + 1];
        if (element1A != element1B || element2A != element2B) {
            deltaE += matriz[element1A][element1B];
            deltaE -= matriz[element2A][element2B];
        }
    }
    return deltaE;
}

int main() {
    int NUM_ITERATIONS = 1E2;
    float temperature, deltaE;
    float T0 = 1;
    float alpha = 3;
    int16_t num_points = 5;


    vector<vector<float>> matrix(num_points, vector<float>(num_points));

    int16_t sequence[num_points] = {1, 3, 4, 2, 5};
    int16_t sequence2[num_points] = {1, 2, 4, 3, 5};

    ifstream arquivo("banco_de_dados//matriz_random.txt");
    for (int r = 0; r < num_points; r++) {
        for (int c = 0; c < num_points; c++) {
            arquivo >> matrix[r][c];
        }
    }


    deltaE = calculate_deltaE(matrix, sequence, sequence2, num_points);
    cout << deltaE;

    // rest of the code
}
