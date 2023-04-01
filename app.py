from flask import Flask, request, render_template
from data import read_csv_file, data_manipulation, plot_graphs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field = request.form['field']
        csv_file = request.files['file']
        if not csv_file:
            return 'No file uploaded.', 400
        df, dates, agent_ids, fields = read_csv_file(csv_file)
        df_filtered = data_manipulation(df, dates, agent_ids, fields, field)
        plot = plot_graphs(df_filtered)
        return render_template('graph.html', image = plot)
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)