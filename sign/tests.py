from django.test import TestCase
from sign.models import Event, Guest
from django.contrib.auth.models import User


# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        """创建数据"""
        Event.objects.create(id=3, name="oneplus 3 event", status=True, limit=2000,
                             address='shenzhen', start_time='2016-08-31 02:08:12')
        Guest.objects.create(id=7, event_id=3, real_name='alen',
                             phone='18680942177', email='lili@dian.so', sign='False')

    def test_event_models(self):
        """查询创建数据"""
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, 'shenzhen')
        self.assertTrue(result.status)

    def test_guest_models(self):
        """查询创建数据"""
        result = Guest.objects.get(phone='18680942177')
        self.assertEqual(result.real_name, 'alen')
        self.assertFalse(result.sign)


class IndexPageTest(TestCase):
    """测试index登录首页"""

    def test_index_page_renders_index_template(self):
        """测试index视图"""
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    """测试登录动作"""

    def setUp(self):
        User.objects.create_user('admin1', 'admin1@mial.com', 'admin123')

    def test_add_admin(self):
        """测试添加用户"""
        user = User.objects.get(username='admin1')
        self.assertEqual(user.username, 'admin1')
        self.assertEqual(user.email, 'admin1@mial.com')

    def test_login_action_username_password_null(self):
        """用户密码为空"""
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        """用户密码"""
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/login_action', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        """登录成功"""
        test_data = {'username': 'admin1', 'password': 'admin123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):
    """发布会管理"""

    def setUp(self):
        User.objects.create_user('admin2', 'admin2@mial.com', 'admin123')
        Event.objects.create(name='xiaomi5', limit=2000, address='beijing', status=1, start_time='2017-08-10 12:20:11')
        self.login_user = {'username': 'admin2', 'password': 'admin123'}

    def test_event_manage_success(self):
        """测试发布会:xiaomi5"""
        response = self.client.post('/login_action', data=self.login_user)
        response = self.client.post('/event_manage')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_vent_manage_search_success(self):
        """测试发布会搜索"""
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {'name': 'xiaomi5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)


class GuestManageTest(TestCase):
    """嘉宾管理"""

    def setUp(self):
        User.objects.create_user('admin1', 'admin1@mial.com', 'admin123')
        Event.objects.create(id=4, name='xiaomi5', limit=2000, address='beijing', status=True,
                             start_time='2017-08-10 12:20:11')
        Guest.objects.create(real_name='ala', phone='18716728377', email='ala@email.com', sign='False', event_id=4)
        self.login_user = {'username': 'amdin1', 'password': 'admin123'}

    def test_event_models(self):
        """查询创建嘉宾数据"""
        result = Event.objects.get(name='xiaomi5')
        self.assertEqual(result.address, 'beijing')
        self.assertTrue(result.status)

    def test_guest_models(self):
        """查询嘉宾创建数据"""
        result = Guest.objects.get(phone='18716728377')
        self.assertEqual(result.real_name, 'ala')
        # print(result.real_name)
        self.assertFalse(result.sign)

    def test_event_manage_success(self):
        """测试嘉宾信息：ala"""
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ala', response.content)
        self.assertIn(b'18716728377', response.content)

    #
    # def test_guest_manage_search_success(self):
    #     """测试嘉宾搜索"""
    #     response = self.client.post('/login_action/', data=self.login_user)
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.post('/search_phone/', {'phone': '11112321234'})
    #     self.assertIn(b'ala', response.content)
    #     self.assertIn(b'18716728377', response.content)

    class SignIndexActionTest(TestCase):
        """发布会签到"""

        def setUp(self):
            User.objects.create_user('admin', 'admin@email.com', 'admin123')
            Event.objects.create(id=1, name='xiaomi5', limit=2000, address='beijing',
                                 status=False, start_time='2017-8-10 12:30:00')
            Event.objects.create(id=2, name='xiaomi4', limit=2000, address='shanghai',
                                 status=False, start_time='2016-8-9 12:30:00')
            Guest.objects.create(real_name='qiaoba', phone='18976542373', email='qiaoba@mail.com',
                                 sign=True, event_id=1)
            Guest.objects.create(real_name='yedou', phone='18976542372', email='yedou@mail.com',
                                 sign=False, event_id=2)
            self.login_user = {'username': 'admin', 'password': 'admin123'}

        def test_sign_index_action_phone_null(self):
            """手机号为空"""
            response = self.client.post('/login_action/', data=self.login_user)
            response = self.client.post('/sigin_index_action/1/', {'phone': ''})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'phone error.', response.content)

        def test_sign_index_action_phone_or_event_id_error(self):
            """手机号或发布会id错误"""
            response = self.client.post('/login_action/', data=self.login_user)
            response = self.client.post('/sigin_index_action/2/', {'phone': '18680942183'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'event id or phone error.', response.content)

        def test_sign_index_action_user_sign_has(self):
            """用户已签到"""
            response = self.client.post('/login_action', data=self.login_user)
            response = self.client.post('/sign_index_action/2/', {'phone': '18976542372'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'user has sign in.', response.content)

        def test_sign_index_action_sign_success(self):
            """签到成功"""
            response = self.client.post('/login_action/', data=self.login_user)
            response = self.client.post('/sign_index_action/1/', {'phone': '18976542373'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'sign in success!', response.content)

