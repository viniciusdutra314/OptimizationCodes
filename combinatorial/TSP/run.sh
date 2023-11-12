dados=$1
ponto_a=$2
ponto_b=$3
visualizacao=$4
algoritmo=$5
echo 'Bem vindo ao TSP'

start=$(date +%s%N)
shortest_path=$(python3 algorithms/$algoritmo.py --data "$dados" --start "$ponto_a" --end "$ponto_b")
end=$(date +%s%N)
delta_t=$(echo "scale=2; ($end - $start) / 1000000000" | bc)
echo Melhor caminho encontrado: $shortest_path 
echo Execução do algoritmo: $delta_t segundos

start=$(date +%s%N)
python3 visualização//plot_$visualizacao.py --shortestpath "$shortest_path" --data "$dados" --start "$ponto_a" --end "$ponto_b"
end=$(date +%s%N)
delta_t=$(echo "scale=2; ($end - $start) / 1000000000" | bc)
echo Execução da visualização: $delta_t segundos