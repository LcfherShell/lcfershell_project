from routers.setting import *
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
import sys


#user = Store(username='lemonrrq', picture=None, product='Laptop Asus xxi932', category='electronic', price=5000000, sold=None, stock=12, descrip='jual cepat')
#guest = Store(username='alexander', picture=None, product='Susu Bearbrand', category='minuman', price=10000, sold=12, stock=500, descrip='minuman sehat penumbuh tulang')
#db.session.add(user)
#db.session.add(guest)
#db.session.commit()


####
#user = input('cari data: ')
#records = db.session.query(Store).filter(Store.product.like("%"+user+"%")).all()
#for i in records:
#    print(i.username, i.product, i.category, i.sold, i.price, i.stock, i.descrip)

#product = Store.query.all()
#print(product)
#results =db.session.query(User, Store).join(Store).all()
#for user, store in results: 
#    print(user.avatar, user.username, store.product, store.category, store.price, store.sold, store.stock, store.descrip)


app = Flask(__name__)
basedir = os.path.dirname((os.path.abspath(__file__)))
UPLOAD_FOLDER = basedir+'/static/download'
app.config.update(dict( 
    SECRET_KEY = os.urandom(58),
    SECURITY_PASSWORD_SALT = os.urandom(128),
    PERMANENT_SESSION_LIFETIME = timedelta(days=2),
    OAUTHLIB_INSECURE_TRANSPORT= True,
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_PUBLIC_KEY = RECAPTCHA['key'],
    RECAPTCHA_PRIVATE_KEY = RECAPTCHA['secret'], 
    SQLALCHEMY_DATABASE_URI = database, 
    SQLALCHEMY_TRACK_MODIFICATIONS = True,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 25,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "<your_Email>",
    MAIL_PASSWORD = "<Your_Password_Email>'",
    UPLOAD_FOLDER = UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024,
))

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_image(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db = SQLAlchemy(app)
oauth = OAuth(app)
recaptcha = ReCaptcha()
recaptcha.init_app(app)
tokens = URLSafeTimedSerializer(app.secret_key)
mail = Mail(app)
otp=randint(000000,999999)
date = datetime.now()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    avatar   = db.Column(db.LargeBinary)
    email    = db.Column(db.String(100))
    password = db.Column(db.String(224))
    auth     = db.Column(db.String(224))
    level    = db.Column(db.String(10)) 
    def __init__(self, username, avatar, email, password, auth,level):
        self.username = username
        self.avatar = avatar
        self.email = email
        self.password = password
        self.auth  = auth
        self.level  = level
    def __repr__(self):
        return '<User %r>' % self.username

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('user.username'))
    picture   = db.Column(db.String(224))
    product  = db.Column(db.String(120))
    brand  = db.Column(db.String(120))#brands #type
    category = db.Column(db.String(224), db.ForeignKey('categ.category'))
    price    = db.Column(db.Integer)#harga
    sold     = db.Column(db.Integer)#terjual
    stock    = db.Column(db.Integer)
    descrip  = db.Column(db.String(120))
    date     = db.Column(db.String(120))
    def __init__(self, username, picture, product, brand, category, price, sold, stock, descrip, date):
        self.username = username
        self.picture = picture
        self.product = product
        self.brand = brand
        self.category = category
        self.price  = price
        self.sold  = sold
        self.stock = stock
        self.descrip = descrip
        self.date = date
    def __repr__(self):
        return '<Product %r>' % self.product

class Categ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120))
    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return '<Product %r>' % self.product

class Costumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('user.username'))
    seller   = db.Column(db.String(100), db.ForeignKey('seller.username'))
    product  = db.Column(db.String(120), db.ForeignKey('store.product'))
    price    = db.Column(db.Integer)
    payment  = db.Column(db.String(25))
    total    = db.Column(db.Integer)
    def __init__(self, username, seller, product, price, payment, total):
        self.username = username
        self.seller = seller
        self.product = product
        self.price   = price
        self.payment = payment
        self.total  = total
    def __repr__(self):
        return '<Total %r>' % self.total

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('user.username'))
    product  = db.Column(db.String(120), db.ForeignKey('store.product'))
    payment  = db.Column(db.String(25))
    status   = db.Column(db.String(25))
    confirm  = db.Column(db.String(25))
    def __init__(self, username, product, payment, status, confirm):
        self.username = username
        self.product = product
        self.payment = payment
        self.status  = status
        self.confirm  = confirm
    def __repr__(self):
        return '<Product %r>' % self.product

class Api(db.Model):
    username = db.Column(db.String(100), db.ForeignKey('user.username'))
    key  = db.Column(db.String(25), primary_key=True)
    secret = db.Column(db.String(125))
    def __init__(self, username, key, secret):
        self.username = username
        self.key = key
        self.secret = secret
    def __repr__(self):
        return '<Username %r>' % self.username

class Blog(db.Model):
   username = db.Column(db.String(100), db.ForeignKey('user.username'), primary_key=True)
   title  = db.Column(db.String(125))
   files   = db.Column(db.LargeBinary)
   def __init__(self, username, title, files):
        self.username = username
        self.title = title
        self.files = files
   def __repr__(self):
        return '<Username %r>' % self.username

##costummer #chat and vicall
github = oauth.remote_app(
    name = 'github',
    consumer_key= GITHUB['key'] ,#'b4441aac9278439c72ed',
    consumer_secret= GITHUB['secret'] ,#'efee60300dd6c1810f37f3f970c069e7e1f6ea62',
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

google = oauth.remote_app(
    name = 'google',
    consumer_key= GOOGLE['key'] ,#'48161273198-k268u9r7n5mlhrbdrpj8qss56vqht9qp.apps.googleusercontent.com',
    consumer_secret= GOOGLE['secret'] , #'65vVDEjHu4si0BMoEKiWIRKs',
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/', methods=['GET'])
def index(): 
    username = session.get('username')
    limit = 10
    no = None
    records = Store.query.paginate(per_page=limit, error_out=False)
    #if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER']+'/image', product.picture)):
    if username is not None:
        user= username
    else:
        user = None
    return render_template('index.jinja',no=no,  user=user, date=date, records=records, ConvertMany=ConvertMany, os=os, app=app)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.jinja', date=date)
####################################################################### Form 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogForm(request.form)
    pages = 'LOGIN'
    if request.method == 'POST' and form.validate_on_submit():
        name  = form.user.data
        pas    = form.password.data
        user = MasterSec(name+pas)
        if user.XsSecForm_Default() == True:
           keylist = Hashing(pas, "sha224")
           data = User.query.filter_by(username=name, password=keylist.Hasher()).first()
           if data is not None:
                 session['access'] = name
                 session['username'] = clean(name)
                 user =  session['username']
                 #login_user(data, remember=form.recaptcha.data)
                 print("Username:\033[0;32m"+name+"\033[0m Password:\033[0;32m"+keylist.Hasher()+"\033[0m")
                 return redirect(url_for('dashboard'))
        else: 
           print ("\033[0;31manda menggunakan special character\033[0m")

    if 'username' in session:
        user =  session['username']
        return redirect(url_for('dashboard'))

    return render_template('login.jinja', form=form, pages=pages)

@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegForm(request.form)
    pages = 'REGISTER'
    if request.method == 'POST' and form.validate_on_submit():
        namef  = form.name_first.data
        namel  = form.name_last.data
        email  = form.email.data
        pas    = form.password.data
        user = MasterSec(namef+namel)
        mail = MasterSec(email)
        pasz = MasterSec(pas)
        if user.XsSecForm_Default() == True and mail.XsSecForm_Default() == True and pasz.XsSecForm_Default() == True :
              keylist = Hashing(pas, "sha224")
              username  = namef+namel
              level='user'        
              data = User.query.filter_by(username=username, email=email).first()
              dataname = User.query.filter_by(username=username).first()
              dataemail = User.query.filter_by( email=email).first()
              if data is None and  dataname is None and  dataemail is None:
                      user = User(username, None, email, keylist.Hasher(), None, level)#level
                      db.session.add(user)
                      db.session.commit()
                      #login_user(user, remember=form.recaptcha.data)

                      ##############################################################################flask
                      print("Username:\033[0;32m"+namef+" "+namel+"\033[0m  Email:\033[0;32m"+email+"\033[0m Password:\033[0;32m"+keylist.Hasher()+"\033[0m")
                      
                      #session['access'] = namef
                      #session['username'] = namef+namel
                      #user =  session['username']
                      return redirect(url_for('login'))
              else:
                      flash('A user with that email address or username already exists.')
           
        else:
           print(user.XsSecForm_Clean())
           print(mail.XsSecForm_Clean())
           print(pasz.XsSecForm_Clean()) 
           print ("\033[0;31manda menggunakan special character\033[0m")
    if 'username' in session:
        #user =  session['access']
        return redirect(url_for('login'))#, user=user))
    return render_template('register.jinja', form=form, pages=pages)

@app.route('/dashboard')
#@login_required
def dashboard():
    user = session.get('username')
    if user is not None:
        data = User.query.filter_by(username=user).first()
        id=data.id
        username = data.username
        avatar = data.avatar
        email = data.email
        level = data.level

        strorelist = Store.query.all()
        numberstore = len(strorelist)
        numberst    = range(len(strorelist))

        userlist = User.query.all()
        numberuser = len(userlist)
        number = range(len(userlist))

        getcostumer = Costumer.query.all()
        numbercostumer = len(getcostumer)
        numbercost = range(len(getcostumer))

        getreseller = Seller.query.all()
        numberseller = len(getreseller)
        numbersel = range(len(getreseller))

        sellerlist = Seller.query.filter_by(username=user).first()
        costumerlist = Costumer.query.filter_by(username=user).first()
        #joins =db.session.query(User, Store).join(Store).all()
        return render_template('dashboard.jinja', id=id, username=username ,avatar=avatar ,email=email, level=level, \
             userlist=userlist, number=number, numberuser=numberuser, date=date, sellerlist=sellerlist, costumerlist=costumerlist, \
             getcostumer=getcostumer, numbercostumer=numbercostumer, numbercost=numbercost, getreseller=getreseller, numberseller=numberseller,\
             numbersel=numbersel, strorelist=strorelist, numberstore=numberstore, numberst=numberst)
    return redirect(url_for('login'))
    
@app.route('/dashboard/add/user', methods=['GET', 'POST'])
def useradd():
    form = RegForm(request.form)
    pages = 'ADD USER'
    user = session.get('username')
    if user is None:
        return redirect(url_for('login'))

    select = User.query.filter_by(username=user).first()
    level = select.level
    if request.method == 'POST' and form.validate_on_submit():
        namef  = form.name_first.data
        namel  = form.name_last.data
        email  = form.email.data
        pas    = form.password.data
        user = MasterSec(namef+namel)
        mail = MasterSec(email)
        pasz = MasterSec(pas)
        if user.XsSecForm_Default() == True and mail.XsSecForm_Default() == True and pasz.XsSecForm_Default() == True :
              keylist = Hashing(pas, "sha224")
              sha244 = keylist.Hasher()
              username  = namef+namel
              level='user'        
              #data = User.query.filter_by(username=username, email=email).first()
              dataname = User.query.filter_by(username=username).first()
              dataemail = User.query.filter_by( email=email).first()
              if dataname is None and dataemail is None:
                      user = User(username, None, email, keylist.Hasher(), None, level)#level
                      db.session.add(user)
                      db.session.commit()
                      #login_user(user, remember=form.recaptcha.data)

                      ##############################################################################flask
                      print("Username:\033[0;32m"+namef+" "+namel+"\033[0m  Email:\033[0;32m"+email+"\033[0m Password:\033[0;32m"+keylist.Hasher()+"\033[0m")
                      
                      #session['access'] = namef
                      #session['username'] = namef+namel
                      #user =  session['username']
                      return redirect(url_for('dashboard'))
              else:                   
                      flash('A user with that email address or username already exists.')
              return render_template('adduser.jinja', form=form, pages=pages)
        else:
           print(user.XsSecForm_Clean())
           print(mail.XsSecForm_Clean())
           print(pasz.XsSecForm_Clean()) 
           print ("\033[0;31manda menggunakan special character\033[0m")
    
    if not level == 'admin':
        #user =  session['access']
        return redirect(url_for('dashboard'))#, user=user))
    
    return render_template('adduser.jinja', form=form, pages=pages)

    
@app.route('/dashboard/<int:id>/update', methods=['GET', 'POST'])
def userupdate(id):
    form = UserUpdate(request.form)
    ###################################
    user = session.get('username')
    data = User.query.filter_by(id=id).first()
    select = User.query.filter_by(username=user).first()#select session
    userlist = User.query.all()
    numberuser = len(userlist)
    number = range(len(userlist))
    #print(numberuser)
    #for nums in number:
    #    if nums is not 0:
    #       data = User.query.filter_by(id=nums).first()
    #       print(data.id)
    
    if data and select:
        level   = data.level
        level2  = select.level
    else:
        return redirect(url_for('dashboard'))

    if level == 'admin':
        return redirect(url_for('dashboard'))

    if user is None:
        return redirect(url_for('login'))


    if level2 == 'admin':
       username = data.username
       email = data.email

    else:
        if data.username == user:
             username = select.username
             email = select.email
        else:
             return redirect(url_for('dashboard'))

    if request.method == 'POST' and form.validate_on_submit():
         name = form.username.data
         email  = form.email.data
         pas    = form.password.data
         keylist = Hashing(pas, "sha224")
         sha244 = keylist.Hasher()
         avatar = None
         filuser = MasterSec(name)
         filmail = MasterSec(email) 
         filpas = MasterSec(pas)
         user = User.query.get_or_404(id) ## Announcements.query.get(id)
         if filuser.XsSecForm_Default() == True and filmail.XsSecForm_Default() == True and filpas.XsSecForm_Default() == True:   
            if User.query.filter_by(username=name).first() is None:
                 user.username = name###satu persatu
                 user.avatar = avatar
                 user.email = email
                 user.password = keylist.Hasher()
                 db.session.commit()
                 user = session.get('username')
                 select = User.query.filter_by(username=name).first()
                 level = select.level

                 ###############select
                 if Costumer.query.filter_by(username=user).first():
                      costumer = Costumer.query.filter_by(username=user).update(dict(username=name))
                      db.session.commit()
                 if Seller.query.filter_by(username=user).first():
                      seller = Seller.query.filter_by(username=user).update(dict(username=name))
                      db.session.commit()    
                 if Store.query.filter_by(username=user).first():
                      store = Store.query.filter_by(username=user).update(dict(username=name))
                      db.session.commit()

                 if not level == 'admin':        
              ###############session       
                    session['access'] = form.username.data
                    session['username'] = form.username.data
                    user =  session['username']
                 return redirect(url_for('dashboard'))

            else:
                 db.session.rollback()
                 return redirect(url_for('dashboard'))

    return render_template('uupdate.jinja', form=form, email=email, username=username)

@app.route("/dell/<option>", methods=["GET"])
def dellUser(option):
  user = session.get('username')
  data = User.query.filter_by(username=user).first()
  if user is None:
      return redirect(url_for('login'))
  if data.level == 'admin':
      return redirect(url_for('login'))
  else:
     if option == 'user':
         db.User.query.delete()
         db.session.commit()
         admin = User('deddycorbuzer', 'default.jpg', 'ramsyantungga1234@gmail.com','9b3e61bf29f17c75572fae2e86e17809a4513d07c8a18152acf34521', None, 'admin')
         db.session.add(admin)
         db.session.commit()
     elif option == 'seller':
         db.Seller.query.delete()
         db.session.commit()
         try:
            db.Costumer.query.delete()
            db.session.commit()
         except:
            pass
     elif option == 'costumer':
         db.Costumer.query.delete()
         db.session.commit()

@app.route("/dashboard/<int:id>/delete", methods=["GET"])
def userdelete(id):
    num = id
    user = session.get('username')
    select = User.query.filter_by(username=user).first()#select session
    #db.session.delete(data)
    #db.session.commit()
    if select:
         if select.level == 'admin':
             data = User.query.filter_by(id=num).first()
             level   = data.level
         else:
             validate = User.query.filter_by(id=num).first()
             if validate.username == user:
                data = User.query.filter_by(username=user).first()
                level   = data.level
             else:
                 flash('Invalid !'+str(num))
                 return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('dashboard'))

    if user is None:
        return redirect(url_for('login'))

    if level == 'admin':
        return redirect(url_for('dashboard'))

    if not level == 'admin':
        if Store.query.filter_by(username=user).first():
             store = Store.query.filter_by(username=user).first()
             if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER']+'/image', store.picture)): 
                os.unlink(os.path.join(app.config['UPLOAD_FOLDER']+'/image', store.picture))
             db.session.delete(store)
             db.session.commit()

        if Costumer.query.filter_by(username=user).first():
             data = Costumer.query.filter_by(username=user).first()
             db.session.delete(data)
             db.session.commit()
        if Seller.query.filter_by(username=user).first():
             seller = Seller.query.filter_by(username=user).first()
             if Costumer.query.filter_by(product=seller.product).first():
                 costumer = Costumer.query.filter_by(product=seller.product).first()
                 db.session.delete(costumer)
                 db.session.commit()
             db.session.delete(seller)
             db.session.commit()
        db.session.delete(data)
        db.session.commit()
        #del session['access']
        #del session['username']

    if not user == 'deddycorbuzer':
       del session['access']
       del session['username']
       return redirect(url_for('index'))
        
    return redirect(url_for('dashboard'))


@app.route('/reset/<email>', methods=["POST", "GET"])
def reset(email):
    user = session.get('username')
    if user is not None:
        return redirect(url_for('dashboard'))

    data = User.query.filter_by(email=email).first()
    if data is None:
        return "Not Email: "+str(email)

    if data.level == 'admin':
        return redirect(url_for('login'))

    hashing = Hashing(str(data.id), "base64Encode")
    number = hashing.Hasher()
    session['id']=str(number)
    email   =  data.email
    token = tokens.dumps(email, salt='email-confirm')
    link  = url_for('resetnow', token=token, x=str(number),  _external=True) 
    #msg = Message("Send Mail Tutorial!",
	#	  sender="yoursendingemail@gmail.com",
	#	  recipients=["recievingemail@email.com"])
	#msg.body = "Yo!\nHave you heard the good word of Python???"           
	#mail.send(msg)
    print(url_for('resetnow', token=token, x=str(number),  _external=True))
    print(session['id'])
    md = str(otp)
    sms = str(link)+md
    print(sms)
    return redirect(link)

@app.route('/reset/confirm/<token>/<x>', methods=["POST", "GET"])
def resetnow(token, x):
    user = session.get('username')
    cookie = session.get('id')
    form = ResetPass(request.form)
    token = token
    msg = "You can't access the token, maybe your token is wrong or has expired"

    if cookie is not None:
        hashing = Hashing(str(cookie), "base64Decode")
        o = hashing.Hasher()
        id = str(o)
    else:
        return redirect(url_for('login'))
    
    if user is not None:
        return redirect(url_for('dashboard'))
    
    try:
        data = tokens.loads(token, salt='email-confirm', max_age=100)

    except SignatureExpired:
        data = None
        flash(msg)
        return redirect(url_for('login'))

    except BadSignature:
        data = None
        flash(msg)
        return redirect(url_for('login'))
    
    except BadTimeSignature:
        data = None
        flash(msg)
        return redirect(url_for('login'))
    
    if request.method == 'POST' and form.validate_on_submit():
         code = form.code.data
         pas    = form.password.data
         filcode = MasterSec(code)
         filpas = MasterSec(pas)
         user = User.query.get_or_404(id)
         if filcode.XsSecForm_Default() == True and filpas.XsSecForm_Default() == True:
             if otp == int(code):
                 user.password = pas
                 db.session.commit()
                 del session['id']
                 return redirect(url_for('login'))
    return render_template('resetpass.jinja', form=form)

  
@app.route('/logout')
def logout():
    if 'username' in session:
         del session['access'] ####dirubah dari status online ke offline
         del session['username']
    return redirect(url_for('index'))




@app.route('/access/github')
def gitauth():
    return github.authorize(callback=url_for('git_call' , _external=True))

@app.route('/access/github/auth')
def git_call():
    resp = github.authorized_response()
    session['access'] = (resp['access_token'], '')
    me = github.get('user')
    username = me.data['name']
    if User.query.filter_by(username=username).first() is None:
         level =  'user'
         user = User(username, None, None, None, None, level)#level
         db.session.add(user)
         db.session.commit()
         session['username'] = username
    else:
        session['username'] = username

    #company = me.data['company']
    if 'username' in session:
           flash('Login Github')
           return redirect(url_for('dashboard'))

    return redirect(url_for('dashboard'))

###########aouth
@app.route('/access/google')
def goauth():
    return google.authorize(callback=url_for('go_call', _external=True))

@app.route('/access/google/auth')
def go_call():
    resp = google.authorized_response()
    session['access'] = (resp['access_token'], '')
    me = google.get('userinfo')
    email = me.data['email']
    username = clean(email)
    if User.query.filter_by(username=username).first() is None:
         level =  'user'
         user = User(username, None, None, None, None, level)#level
         db.session.add(user)
         db.session.commit()
         session['username'] = username
    else:
        session['username'] = username


    if 'username' in session:
           return redirect(url_for('dashboard'))
    return redirect(url_for('dashboard'))


@github.tokengetter
def get_github_oauth_token():
    return session.get('access')

@google.tokengetter
def get_google_oauth_token():
    return session.get('access')


#############pages

##########mychaneel tutotial lcfershell

@app.route('/clock')
def clock(): 
    return render_template('clock.jinja')


#######tutup sementara
@app.route('/weatcher')
def weatch():
    vet = nclean(temperatur) 
    return "Location: "+loc+" Temperatur:"+vet+"°C Pressure:"+pressure+' Deskription:'+clouds

@app.route('/speed', methods=['GET','POST'])
def speed():
    if request.method == 'POST':
        print("-->Download Speed: {:.2f} Kb/s\n-->Upload Speed: {:.2f} Kb/s\n-->Ping: {}\n-->ISP: {}, {}".format(download,upload,ping, client,country))
        return render_template('testconnection.jinja', ip4=ip4, download=download, upload=upload, ping=ping, clients=client, countrys=country)
    else:
        return render_template('testconnection.jinja', download=0, upload=0,ping=0, ip4='None', client="None", country="None") 

@app.route('/covid')
def covid():
    return render_template('covid19.jinja', countries=countries, wcovid=wcovid, ConvertMany=ConvertMany)

    

########################################appstore
@app.route('/dashboard/add/product/', methods=['GET','POST'])
def addproduct():
    listcategory = Categ.query.all()
    user = session.get('username')
    if user is None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        product = request.form['product']
        brand = request.form['brand']
        category = request.form['category']
        price = request.form['prices']
        payment = request.form['payment']
        sold =  None
        stock = request.form['stocts']
        descrip = request.form['descrip']

        print(stock)
        filcode = MasterSec(product+brand)
        filpas = MasterSec(category)
 

        if filcode.XsSecForm_Default() == True and filpas.XsSecForm_Default() == True:
            date = datetime.now()
            getdate = str(date.day)+"-"+str(date.month)+"-"+str(date.year)
            # check if the post request has the files part
            if 'files' not in request.files:
                 flash('No file part')
            files = request.files['files']
            files.filename = key_gen(ExtFiles(files.filename, 'name'), clean='clean')+'.'+ExtFiles(files.filename, 'ext')
            #print(key_gen(ExtFiles(files.filename, 'name'), clean='clean')+'.'+ExtFiles(files.filename, 'ext'))
            print(product+"  "+brand+" "+category+" "+descrip)
            if files and allowed_image(files.filename):
                 filename = secure_filename(files.filename)
                 files.save(os.path.join(app.config['UPLOAD_FOLDER']+'/image', filename))
                 flash('Successfully uploaded')
                 saves = Store(user, files.filename, product, brand , category, price, sold, stock, descrip, getdate)
                 db.session.add(saves)
                 db.session.commit()
                 if Seller.query.filter_by(product=product).first() is None:
                      seller = Seller(user, product, payment, 'available', None)
                      db.session.add(seller)
                      db.session.commit()

                
    return render_template('additems.jinja', listcategory=listcategory)
    


@app.route('/dashboard/seller/data/<page>', methods=['GET','POST'], defaults={"page":1})
def myseller(page):
    limit = 5
    user = session.get('username')
    seller = Store.query.all()
    roundseller = range(len(seller))
    costumer = Costumer.query.all()
    roundcostumer = range(len(costumer))
    token = str(otp)
    if user is None:
        return redirect(url_for('login'))
    if Seller.query.filter_by(username=user).first() is None: 
        return redirect(url_for('dashboard'))

    if page:
                records = Store.query.paginate(page=page,per_page=limit, error_out=False)
    else:
                records = Store.query.paginate(per_page=limit, error_out=False)
    return render_template('seller.jinja', records=records, user=user, seller=seller, roundseller=roundseller,\
         costumer=costumer, roundcostumer=roundcostumer, ConvertMany=ConvertMany, token=token)


@app.route('/dashboard/costumer/data/<page>', methods=['GET','POST'], defaults={"page":1})
def mycostumer(page):
    limit = 5
    user = session.get('username')
    costumer = Costumer.query.all()
    number = len(costumer)
    roundcostumer = range(len(costumer))
    token = str(otp)
    if user is None:
        return redirect(url_for('login'))
    if Costumer.query.filter_by(username=user).first() is None: 
        return redirect(url_for('dashboard'))

    return render_template('costumer.jinja', user=user, \
        costumer=costumer, number=number, roundcostumer=roundcostumer, ConvertMany=ConvertMany, token=token)


#######perbaikan
@app.route('/product/options/confirm/<int:id>', methods=['GET'])
def rundelete(id):
    user = session.get('username')
    if user is None:
        return redirect(url_for('login'))
    if Costumer.query.filter_by(id=id).first() is None:
        return redirect(url_for('dashboard'))
   
    if user == 'deddycorbuzer':
       costumer = Costumer.query.filter_by(id=id).first()
       db.session.delete(costumer)
       db.session.commit()
    elif Costumer.query.filter_by(id=id).first():
       costumer = Costumer.query.filter_by(id=id).first()
       db.session.delete(costumer)
       db.session.commit()
    else:
       costumer = Costumer.query.filter_by(id=id, username=user).first()
       db.session.delete(costumer)
       db.session.commit()

    flash('success!')
    return redirect(url_for('dashboard'))








####################################################################
@app.route('/product/option/<int:id>/update')
@app.route('/product/option/<int:id>/update/', methods=["POST", "GET"])
def upproduct(id):
    user = session.get('username')
    if user is None:
        return redirect(url_for('login'))
    
    if Store.query.filter_by(id=id, username=user).first() is None:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        product = request.form['product']
        brand = request.form['brand']
        category = request.form['category']
        price = request.form['prices']
        sold =  None
        stock = request.form['stocts']
        descrip = request.form['descrip']
        filcode = MasterSec(product+brand)
        filpas = MasterSec(category)
        if filcode.XsSecForm_Default() == True and filpas.XsSecForm_Default() == True:
                if 'files' not in request.files:
                    flash('No file part')
                stores = Store.query.filter_by(id=id).first()
                product = stores.product
                prices = stores.price
                stocks = stores.stock
                brands = stores.brand
                files = request.files['files']
                files.filename = key_gen(ExtFiles(files.filename, 'name'), clean='clean')+'.'+ExtFiles(files.filename, 'ext')
                    #print(key_gen(ExtFiles(files.filename, 'name'), clean='clean')+'.'+ExtFiles(files.filename, 'ext'))
                if files and allowed_image(files.filename):
                         filename = secure_filename(files.filename)
                         files.save(os.path.join(app.config['UPLOAD_FOLDER']+'/image', filename))
                         if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER']+'/image', stores.picture)): 
                            os.unlink(os.path.join(app.config['UPLOAD_FOLDER']+'/image', stores.picture))

                if Costumer.query.filter_by(seller=user, product=product).first():
                      data = Costumer.query.filter_by(seller=user, product=product).first()
                      db.session.delete(data)
                      db.session.commit()
                if Seller.query.filter_by(username=user).first():
                      data = Seller.query.filter_by(username=user).update(dict(product=product))
                      db.session.commit() 

                costumer = Store.query.filter_by(username=user).update(dict(picture=files.filename, product=product, brand=brand, category=category, price=price, stock=stock, descrip=descrip, date=dates))
                db.session.commit()
   
        else:
            flash('Failed!')
            db.session.rollback()
            return redirect(url_for('dashboard', product=product, prices=prices, stocks=stocks, brands=brands))
                      
    return render_template('upproduct.jinja')

########################perbaikan################################
@app.route('/product/option/<int:id>/delete', methods=["GET"])
@app.route('/product/option/<int:id>/delete/', methods=["GET"])
def dellproduct(id):
    num = id
    user = session.get('username')
    select = User.query.filter_by(id=num).first()#select session
    #db.session.delete(data)
    #db.session.commit()
    if select:
         if select.level == 'admin':
             if Store.query.filter_by(id=id).first():
                product = Store.query.filter_by(id=id).first()
                if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER']+'/image', product.picture)): 
                    os.unlink(os.path.join(app.config['UPLOAD_FOLDER']+'/image', product.picture))
               
                if Seller.query.filter_by(username=product.username, product=product.product).first():
                        seller = Seller.query.filter_by(username=product.username, product=product.product).first()
                        db.session.delete(seller)
                        db.session.commit()
               
                if Costumer.query.filter_by(seller=product.username, product=product.product).first():
                        costumer = Costumer.query.filter_by(seller=product.username, product=product.product).first()
                        db.session.delete(costumer)
                        db.session.commit()
                db.session.delete(product)
                db.session.commit()
                flash('Delete Product Succes!')
             else:
                flash('Invalid !'+str(num))
                return redirect(url_for('dashboard'))
         else:
             validate = Store.query.filter_by(id=num).first()
             if validate.username == user:
                if Store.query.filter_by(id=id).first():
                     product = Store.query.filter_by(id=id).first()
                     if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER']+'/image', product.picture)): 
                        os.unlink(os.path.join(app.config['UPLOAD_FOLDER']+'/image', product.picture))

                     if Seller.query.filter_by(username=product.username, product=product.product).first():
                        seller = Seller.query.filter_by(username=product.username, product=product.product).first()
                        db.session.delete(seller)
                        db.session.commit()
                     if Costumer.query.filter_by(seller=product.username, product=product.product).first():
                        costumer = Costumer.query.filter_by(seller=product.username, product=product.product).first()
                        db.session.delete(costumer)
                        db.session.commit()

                     db.session.delete(product)
                     db.session.commit()
                     flash('Delete Product Succes!')
                else:
                     flash('Invalid !'+str(num))
              
                return redirect(url_for('dashboard'))

             else:
                 flash('Invalid !'+str(num))
                 return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('dashboard'))

    if user is None:
        return redirect(url_for('login'))

        
    return redirect(url_for('dashboard'))


@app.route('/store', methods=['GET','POST'], defaults={"page":1})
@app.route('/store/<int:page>/', methods=['GET','POST'] )
def store(page):
    categorys = request.args.get('categorys', default = None, type = str )
    brands   = request.args.get('brands', default = None, type = str )
    min     = request.args.get('min', default = None, type = int )
    max     = request.args.get('max', default = None, type = int )
    form = SearchEngine(request.form)
    fo = CategorySearch(request.form)
    #fo.brands.choices = [(data.product, data.product) for data in  Store.query.filter_by(category='drinks and food').all()]
    page = page
    limit = 10
    userlist = Store.query.all()
    number = range(len(userlist))
    print(number)
    if categorys is not None:
        if Store.query.filter_by(category=categorys).first():
              select = Store.query.filter_by(category=categorys).first()
              if select is None:
                  return redirect(url_for('store'))
              category  = select.category
              records = db.session.query(Store).filter(Store.category.like("%"+category+"%")).paginate(per_page=limit, error_out=False)
        else:
            fildata = MasterSec(categorys)
            data = fildata.XsSecForm_Clean()
            if data == False:
                flash(message="Data not found! "+str(categorys))
            else:
                flash(message="Data not found! "+str(data))
                    
            return redirect(url_for('store'))
             
    elif brands is not None:    
        if Store.query.filter_by(brand=brands).first():
              select = Store.query.filter_by(brand=brands).first()
              if select is None:
                 return redirect(url_for('store'))
              brandst = select.brand
              records = db.session.query(Store).filter(Store.brand.like("%"+brandst+"%")).paginate(per_page=limit, error_out=False)
        else:
             fildata = MasterSec(brands)
             data = fildata.XsSecForm_Clean()
             if data == False:
                flash(message="Data not found! "+str(brands))
             else:
                flash(message="Data not found! "+str(data))
            
             return redirect(url_for('store'))

    elif request.method == 'POST' and form.validate_on_submit():
         search = form.search.data
         filsearch = MasterSec(search)
         if filsearch.XsSecForm_Default() == True:
             
             if db.session.query(Store).filter(Store.product.like("%"+search+"%")).all():
                  print(search)
                  records = db.session.query(Store).filter(Store.product.like("%"+search+"%")).paginate(per_page=limit, error_out=False)
                  
             elif db.session.query(Store).filter(Store.category.like("%"+search+"%")).all():
                  print(search)
                  records = db.session.query(Store).filter(Store.category.like("%"+search+"%")).paginate(per_page=limit, error_out=False)
             ###tambah brands
             else:
                  data = filsearch.XsSecForm_Clean()
                  if data == False:
                         flash(message="Data not found! "+str(search))
                  else:
                         flash(message="Data not found! "+str(data))
                  return redirect(url_for('store'))
         else:
             data = filsearch.XsSecForm_Clean()
             if data == False:
                   flash(message="Data not found! "+str(search))
             else:
                   flash(message="Data not found! "+str(data))
                     
             return redirect(url_for('store'))
    
   # elif request.method == 'POST' and fo.validate_on_submit():
    
    else:
         if page:
                records = Store.query.paginate(page=page,per_page=limit, error_out=False)
         else:
                records = Store.query.paginate(per_page=limit, error_out=False)

    messages = "Data not found!"
    #results  = db.session.query(User, Store).join(Store).paginate(per_page=limit, error_out=False)
    return render_template('store.jinja', form=form , fo=fo, categorys=categorys, brands=brands ,records=records, convert=ConvertMany, Not=None, messages=messages)


@app.route('/store/category', methods=['GET','POST'] )
def category():
    fo = CategorySearch(request.form)
    if fo.validate_on_submit():
        if fo.category.data:
             data = fo.category.data
             return redirect(url_for('store', categorys=data))
    return redirect(url_for('store'))


########view product

@app.route('/store/view/<int:id>/product', methods=['GET','POST'] )
def viewsProduct(id):
    userlist = User.query.all()
    numberuser = len(userlist)
    number = range(len(userlist))
    categ = Categ.query.all()
    for nums in number:
        if nums != 0:
           print(nums)
           data = User.query.filter_by(id=nums).first()
    if Store.query.filter_by(id=id).first():
        data = Store.query.filter_by(id=id).first()
        records = Store.query.paginate(per_page=4, error_out=False)
        idproduct = data.id
        seller =  data.username
        picture = data.picture
        product = data.product
        brand = data.brand
        price = ConvertMany(data.price, '.')
        stock = ConvertMany(data.stock, '.')
        description = data.descrip
        uploud =  data.date

    else:
        flash("Data not found!")
        return render_template('error.jinja')

    return render_template('viewproduct.jinja', seller=seller, picture=picture, product=product, brand=brand , ConvertMany=ConvertMany\
        , price=price, stock=stock, description=description, uploud=uploud, os=os, app=app, date=date, idproduct=idproduct, records=records,\
         int=int, str=str, categ=categ)


########buy product
@app.route('/store/buy/product/<int:id>', methods=['GET','POST'] )
def buyProduct(id):
    form=BuyProducts()
    user = session.get('username')
    if user is None:
        return redirect(url_for('login'))
 
    if Store.query.filter_by(id=id).first():
        data = Store.query.filter_by(id=id).first()
        picture = data.picture
        product = data.product
        prices = data.price
        seller = data.username
        stock  = data.stock
    else:
        flash('Data not found!')
        return redirect(url_for('viewsProduct', id=id))

    if request.method == 'POST' and form.validate_on_submit():
       product = product
       amount = form.amount.data
       payment = form.paymen.data
       prices = prices
       getotal  = amount*prices
       total = getotal
       stocks = stock-amount
       solds  = amount+stock

       sellers = Costumer.query.filter_by(username=user, seller=seller, product=product).first()
       if sellers:
            costumer = Costumer.query.filter_by(username=user, seller=seller, product=product).update(dict(total=total+sellers.total))
       else:
           costumer = Costumer(user, seller, product, prices, payment, total)
           db.session.add(costumer)
           db.session.commit()
            
       store = Store.query.filter_by(product=product).update(dict(sold=solds, stock=stocks))
       db.session.commit()
       flash('Your item is in progress!')   
       return redirect(url_for('viewsProduct', id=id))
    return render_template('buyitems.jinja', form=form, stock=stock, picture=picture, seller=seller, prices=prices,\
         product=product, ConvertMany=ConvertMany, date=date, os=os, app=app)

##data
#daily needs[kebutuhan sehari2] electronic[elektronik] drinks and food[minuman dan makanan] fashion 
# Store.query.join(User, (Store.username == User.username)).all()


##########metods trans
if __name__ == "__main__":
     app.run(debug=True)









































































































































































###################################chatvicallapp
























































































































###############developper_apps



























































##################group












































































































###############################video






































###################verification
