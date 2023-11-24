dados=$1
ponto_a=$2
ponto_b=$3
algoritmo=$4
visualizacoes=$5

# Quando pontos iniciais e finais não são especificados
if [ -z "$4" ] && [ -z "$5" ]; then
    algoritmo=$ponto_a
    visualizacoes=$ponto_b
    ponto_a=0
    ponto_b=0
fi

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
python3 algorithms/$algoritmo.py --data "$dados" --start "$ponto_a" --end "$ponto_b"
shortest_path=$(python3 algorithms/$algoritmo.py --data "$dados" --start "$ponto_a" --end "$ponto_b")
end=$(date +%s%N)
delta_t=$(echo "scale=2; ($end - $start) / 1000000000" | bc)
echo Melhor caminho encontrado: $shortest_path 
echo Execução do algoritmo: $delta_t segundos

IFS=',' read -ra VISUALIZACOES <<< "$visualizacoes"
for vis in "${VISUALIZACOES[@]}"; do
    if [ -n "$vis" ]; then
        start=$(date +%s%N)
        python3 visualização/plot_$vis.py --shortestpath "$shortest_path" --data "$dados" --start "$ponto_a" --end "$ponto_b" --algoritmo "$algoritmo"
        end=$(date +%s%N)
        delta_t=$(echo "scale=2; ($end - $start) / 1000000000" | bc)
        echo Execução da visualização $vis: $delta_t segundos
    fi
done

rm -f temp_iterations.txt
rm -f visualização//all_costs.txt