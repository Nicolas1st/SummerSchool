#include<linux/init.h>
#include<linux/module.h>
#include<linux/fs.h>
#include<linux/uaccess.h>


MODULE_LICENSE("GPL");
MODULE_AUTHOR("Nicolas1st");
MODULE_DESCRIPTION("Returns an incremented number on each read");
MODULE_VERSION("Final");
 

int val[1] = {0}; // The copy_to_user function does not accept int as an argument so I worked around like this
int *valp = val;
int major_number;

 

static int dev_open(struct inode *inod, struct file *fil);
static ssize_t dev_read(struct file *filep, char *buf,size_t blen,loff_t *off);
static int dev_release(struct inode *inod, struct file *fil);



static struct file_operations fops =
{
	.read=dev_read,
	.open=dev_open,
	.release=dev_release,
};

 

static int hello_init(void)
{

	major_number = register_chrdev(0, "mydevice", &fops);
	printk(KERN_INFO "major number %d\n", major_number);

	if(major_number<0) {
		printk(KERN_ALERT "My device registration failed.");
	} else {
		printk(KERN_ALERT "My device has been registred\n");
	}

	return 0;

}



static void hello_exit(void)
{

	unregister_chrdev(major_number, "mydevice");
	printk(KERN_ALERT "exit");

}

 

static int dev_open(struct inode *inod, struct file *fil)
{

	printk("KERN_ALERT device has been opened");
	return 0;

}

 

static ssize_t dev_read(struct file *filep, char *buf, size_t len,loff_t *off)
{

	val[0]++;
	copy_to_user(buf, valp, sizeof(val[0]));
	printk("KERN_ALERT Some number has been read from the mydevice");
	return sizeof(val[0]);

}
 


static int dev_release(struct inode *inod, struct file *fil)
{

	printk("KERN_ALERT device has been closed\n");
	return 0;

}



module_init(hello_init);
module_exit(hello_exit);
