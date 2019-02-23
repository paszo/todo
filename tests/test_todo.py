from odoo.tests.common import TransactionCase, tagged

@tagged('-at_install', 'post_install')
class TestTodo(TransactionCase):

    def test_create(self):
        "Create a simple Todo"
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):
        "Clear Done sets to non active"
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertFalse(task.active)
