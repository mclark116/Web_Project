from flask import render_template, url_for, request, redirect

from models import db, Articles, app

@app.route('/')
def index():
    return render_template('experiment.html')

@app.route('/reviews')
def reviews():
    reviews = Articles.query.all()
    return render_template('reviews.html', reviews=reviews)

@app.route('/youtube')
def youtube():
    return render_template('flexgridblock.html')

@app.route('/fullarticle/<id>')
def full(id):
    article = Articles.query.get(id)
    return render_template('fullarticle.html', article=article)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_article(id):
    article = Articles.query.get(id)
    if request.form:
        article.name = request.form['name']
        article.title = request.form['title']
        article.sub_title = request.form['article_subtitle']
        article.body = request.form['description']
        article.url = request.form['url']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', article=article)
    

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.form:
        new_article = Articles(name=request.form['name'], title=request.form['title'],
                        sub_title=request.form['article_subtitle'], body=request.form['description'], url=request.form['url'])
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html')




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')