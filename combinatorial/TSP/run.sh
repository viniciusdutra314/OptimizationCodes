dados=$1
ponto_a=$2
ponto_b=$3
algoritmo=$4
visualizacao=$5

echo 'Bem vindo ao TSP!'
if [ "$dados" == newrandom ]; then 
    python3 banco_de_dados/random_points.py
    dados='random'
fi
if [ "$dados" == random ]; then
    ponto_a=0
    ponto_b=0
fi
start=$(date +%s%N)
shortest_path=$(python3 algorithms/$algoritmo.py --data "$dados" --start "$ponto_a" --end "$ponto_b")
end=$(date +%s%N)
delta_t=$(echo "scale=2; ($end - $start) / 1000000000" | bc)
echo Melhor caminho encontrado: $shortest_path 
echo Execução do algoritmo: $delta_t segundos

if [ -n "$visualizacao" ]; then
    start=$(date +%s%N)
    python3 visualização//plot_$visualizacao.py --shortestpath "$shortest_path" --data "$dados" --start "$ponto_a" --end "$ponto_b"
    end=$(date +%s%N)
    delta_t=$(echo "scale=2; ($end - $start) / 1000000000" | bc)
    echo Execução da visualização: $delta_t segundos
fi

rm -f temp_iterations.txt
