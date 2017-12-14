using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace WpfApp
{
    /// <summary>
    /// MainWindow.xaml の相互作用ロジック
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnTry_Click(object sender, RoutedEventArgs e)
        {
            this.BtnTry.IsEnabled = false;
            Task.Run(() => Thread.Sleep(3000));
            this.BtnTry.IsEnabled = true;

            var operation = new DispatcherTimer(DispatcherPriority.Normal)
            {
                Interval = TimeSpan.FromMilliseconds(5000)
            };
            operation.Tick += new EventHandler(DispatcherTryTimer_Tick);
            operation.Start();
        }

        private void DispatcherTryTimer_Tick(object sender, EventArgs e)
        {
            LblTry.Content = "second";
            Task.Run(() => Thread.Sleep(1000));
            LblTry.Content = "third";
        }
    }
}
